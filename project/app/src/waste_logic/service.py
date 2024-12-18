from typing import List, Set
from queue import Queue
from sqlalchemy.orm import Session
from app.src.schemas import WasteType
from app.src.storages.service import StorageService
from app.src.organizations.service import OrganizationService
from app.src.wsas.service import WSAService
from app.src.paths.service import PathService
from app.src.waste_logic.schemas import (
    WasteTransferRequest,
    WasteGenerationRequest,
    WasteRecycleRequest,
)
from app.src.storages.models import StorageModel
from app.src.paths.models import PathModel
from app.src.wsas.models import WSAModel
from app.src.organizations.models import OrganizationModel
from app.src.waste_logic.utils import Graph, Vertex, Edge, Algorithm, StorageUpdateQuery


class WasteTransferService:
    def __init__(self, db: Session):
        self.db = db
        self.storage_service = StorageService(db)
        self.organization_service = OrganizationService(db)
        self.path_service = PathService(db)
        self.wsa_service = WSAService(db)

    def prepare_data(self, transfer_data: WasteTransferRequest):
        organization: OrganizationModel = self.organization_service.get_by_name(
            transfer_data.organization_name
        )
        if not organization:
            raise ValueError("Organization not found!")
        storage: StorageModel = (
            self.storage_service.get_storage_by_org_id_and_waste_type(
                organization.id, transfer_data.waste_type
            )
        )
        if not storage:
            raise ValueError("Storage not found!")
        paths: List[PathModel] = self.path_service.get_paths_from_org(organization.id)
        if len(paths) == 0:
            raise ValueError("No paths from this organization - can't transfer waste!")
        wsas, wsas_id_set = self.wsa_service.get_wsas_from_paths(paths)
        next_wsas: List[WSAModel] = []
        for wsa in wsas:
            self.recursive_wsa_finder(wsa, wsas_id_set, next_wsas)
        wsas = list(set(wsas + next_wsas))
        paths = list(set(paths + self.iterative_path_finder(wsas)))
        return wsas, paths, storage

    def build_graph(self, transfer_data: WasteTransferRequest):
        wsas, paths, storage = self.prepare_data(transfer_data)
        graph: Graph = self.graph_builder(wsas, paths, transfer_data.waste_type)
        return graph, storage

    def get_queries(self, graph: Graph, quantity: int, sz: int):
        algorithm: Algorithm = Algorithm(graph)
        amount = max(0, min(quantity, sz))
        res = algorithm.generate_queries(amount, algorithm.build_queue())
        remainder: int = res[0]
        queue: Queue = res[1]
        return remainder, queue

    def execute_queries(
        self, remainder: int, queue: Queue, storage: StorageModel, waste_type: WasteType
    ):
        if remainder > 0:
            print("Impossible to unload storage!")
        self.storage_service.update_storage_size(storage.id, remainder)
        while not queue.empty():
            query: StorageUpdateQuery = queue.get()
            storages_of_wsa = self.storage_service.get_storages_by_wsa_id(query.wsa_id)
            s = None
            for ns in storages_of_wsa:
                if ns.waste_type == waste_type:
                    s = ns
                    break
            if s is not None:
                self.storage_service.update_storage_size(s.id, query.new_size)

    def transfer_waste(self, transfer_data: WasteTransferRequest):
        graph, storage = self.build_graph(transfer_data)
        remainder, queue = self.get_queries(graph, transfer_data.quantity, storage.size)
        self.execute_queries(remainder, queue, storage, transfer_data.waste_type)
        return self.storage_service.get_all_storages()

    def recursive_wsa_finder(self, wsa: WSAModel, s: Set[int], wsas: List[WSAModel]):
        paths: List[PathModel] = self.path_service.get_paths_from_wsa(wsa.id)
        for path in paths:
            if path.wsa_end_id not in s:
                next_wsa = self.wsa_service.get_wsa(path.wsa_end_id)
                if next_wsa:
                    wsas.append(next_wsa)
                    s.add(next_wsa.id)
                    self.recursive_wsa_finder(next_wsa, s, wsas)

    def iterative_path_finder(self, wsas: List[WSAModel]):
        paths: List[PathModel] = []
        for i in range(len(wsas)):
            for j in range(len(wsas)):
                if i == j:
                    continue
                path = self.path_service.get_path_from_wsas(wsas[i].id, wsas[j].id)
                if path:
                    paths.append(path)
        return paths

    def graph_builder(
        self, wsas: List[WSAModel], paths: List[PathModel], waste_type: WasteType
    ) -> Graph:
        g: Graph = Graph()
        g = self.build_vertices(wsas, waste_type, g)
        g = self.build_edges(paths, g)
        return g

    def build_vertices(
        self, wsas: List[WSAModel], waste_type: WasteType, g: Graph
    ) -> Graph:
        for wsa in wsas:
            storages: List[StorageModel] = self.storage_service.get_storages_by_wsa_id(
                wsa.id
            )
            b = False
            for storage in storages:
                if storage.waste_type == waste_type:
                    g.add_vertex(wsa.id, Vertex(storage.size, storage.capacity))
                    b = True
                    break
            if not b:
                g.add_vertex(wsa.id, Vertex())
        return g

    def build_edges(self, paths: List[PathModel], g: Graph) -> Graph:
        for path in paths:
            if path.bidirectional:
                g.add_edge(path.wsa_start_id, Edge(path.wsa_end_id, path.length))
                g.add_edge(path.wsa_end_id, Edge(path.wsa_start_id, path.length))
            else:
                if path.organization_id:
                    g.add_edge(0, Edge(path.wsa_start_id, path.length))
                else:
                    g.add_edge(path.wsa_start_id, Edge(path.wsa_end_id, path.length))
        return g


class WasteProcessingService:
    def __init__(self, db: Session):
        self.db = db
        self.storage_service = StorageService(db)
        self.organization_service = OrganizationService(db)
        self.wsa_service = WSAService(db)

    def generate_waste(self, generation_data: WasteGenerationRequest):
        organization: OrganizationModel = self.organization_service.get_by_name(
            generation_data.organization_name
        )
        if not organization:
            raise ValueError("Organization not found!")

        storages: List[StorageModel] = self.storage_service.get_storages_by_org_id(
            organization.id
        )
        if generation_data.waste_type is not None:
            for storage in storages:
                if storage.waste_type == generation_data.waste_type:
                    return [
                        self.storage_service.update_storage_size(
                            storage.id, storage.capacity
                        )
                    ]
            raise ValueError(
                "No storage with the given waste type exist in this organization!"
            )
        else:
            res_list: List[StorageModel] = []
            for storage in storages:
                res_list.append(
                    self.storage_service.update_storage_size(
                        storage.id, storage.capacity
                    )
                )
            if len(res_list) == 0:
                raise ValueError("Organization has no storages!")
            return res_list

    def recycle_waste(self, recycle_data: WasteRecycleRequest):
        wsa: WSAModel = self.wsa_service.get_by_name(recycle_data.wsa_name)
        if not wsa:
            raise ValueError("WSA not found!")

        storages: List[StorageModel] = self.storage_service.get_storages_by_wsa_id(
            wsa.id
        )
        if recycle_data.waste_type is not None:
            for storage in storages:
                if storage.waste_type == recycle_data.waste_type:
                    return [self.storage_service.update_storage_size(storage.id, 0)]
            raise ValueError("No storage with the given waste type exist in this WSA!")
        else:
            res_list: List[StorageModel] = []
            for storage in storages:
                res_list.append(self.storage_service.update_storage_size(storage.id, 0))
            if len(res_list) == 0:
                raise ValueError("WSA has no storages!")
            return res_list
