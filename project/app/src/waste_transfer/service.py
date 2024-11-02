from typing import List, Set
from sqlalchemy.orm import Session
from app.src.storages.service import StorageService
from app.src.organizations.service import OrganizationService
from app.src.wsas.service import WSAService
from app.src.paths.service import PathService
from app.src.waste_transfer.schemas import EdgeModel, GraphModel, VertexModel, WasteTransferRequest, WasteType
from app.src.storages.models import Storage
from app.src.paths.models import Path
from app.src.wsas.models import WSA
from app.src.waste_transfer.utils import Graph, Vertex, Edge

class WasteTransferService:
    def __init__(self, db: Session):
        self.db = db
        self.storage_service = StorageService(db)
        self.organization_service = OrganizationService(db)
        self.path_service = PathService(db)
        self.wsa_service = WSAService(db)

    def transfer_waste(self, transfer_data: WasteTransferRequest):
        # find organization
        organization = self.organization_service.get_by_name(transfer_data.organization_name)
        if not organization:
            raise ValueError("Organization not found!")
        
        # find storage that is going to be unloaded
        storages : List[Storage] = self.storage_service.get_all_storages()
        storage : Storage = None
        for s in storages:
            if (s.organization_id == organization.id) and (s.waste_type == transfer_data.waste_type):
                storage = s
                break
        
        if not storage:
            raise ValueError("Storage not found!")
        
        # find all paths that go from this organization
        paths : List[Path] = self.path_service.get_paths_from_org(organization.id)

        if len(paths) == 0:
            raise ValueError("No paths from this organization - can't transfer waste!")

        # find all wsas that are connected to this organization
        wsas : List[WSA] = []
        wsas_id_set : Set[int] = set()
        for p in paths:
            wsa = self.wsa_service.get_wsa(p.wsa_start_id)
            if wsa:
                wsas.append(wsa)
                wsas_id_set.add(wsa.id)
        
        # for each wsa find all wsas connected to them
        next_wsas : List[WSA] = []
        for wsa in wsas:
            self.recursive_wsa_finder(wsa, wsas_id_set, next_wsas)
        
        wsas = list(set(wsas + next_wsas))

        # for each pair of wsas find a path
        paths = list(set(paths + self.iterative_path_finder(wsas)))

        # build a graph
        graph : Graph = self.graph_builder(wsas, paths, transfer_data.waste_type)

        vertices = {k: VertexModel(sz=v.sz, cap=v.cap) for k, v in graph.vertices.items()}
        edges = {k: [EdgeModel(next=edge.next, length=edge.length) for edge in edge_list] 
                 for k, edge_list in graph.edges.items()}
        
        return GraphModel(vertices=vertices, edges=edges)

    
    def recursive_wsa_finder(self, wsa: WSA, s: Set[int], wsas: List[WSA]):
        paths : List[Path] = self.path_service.get_paths_from_wsa(wsa.id)
        for path in paths:
            if path.wsa_end_id not in s:
                next_wsa = self.wsa_service.get_wsa(path.wsa_end_id)
                if next_wsa:
                    wsas.append(next_wsa)
                    s.add(next_wsa.id)
                    self.recursive_wsa_finder(next_wsa, s, wsas)
    
    def iterative_path_finder(self, wsas: List[WSA]):
        paths : List[Path] = []
        for i in range(len(wsas) - 1):
            for j in range(i + 1, len(wsas)):
                path = self.path_service.get_path_from_wsas(wsas[i].id, wsas[j].id)
                if path:
                    paths.append(path)
        
        return paths

    def graph_builder(self, wsas: List[WSA], paths: List[Path], waste_type: WasteType) -> Graph:
        g : Graph = Graph()
        g = self.build_vertices(wsas, waste_type, g)
        g = self.build_edges(paths, g)
        return g
    
    def build_vertices(self, wsas: List[WSA], waste_type: WasteType, g : Graph) -> Graph:
        for wsa in wsas:
            storages : List[Storage] = self.storage_service.get_storages_by_wsa_id(wsa.id)
            b = False
            for storage in storages:
                if storage.waste_type == waste_type:
                    g.add_vertex(wsa.id, Vertex(storage.size, storage.capacity))
                    b = True
                    break
            if not b:
                g.add_vertex(wsa.id, Vertex())
        return g
    
    def build_edges(self, paths: List[Path], g : Graph) -> Graph:
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
            
