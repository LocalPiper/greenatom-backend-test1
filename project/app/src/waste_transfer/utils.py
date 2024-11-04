from typing import List
from queue import Queue, PriorityQueue
from app.src.paths.models import Path
from app.src.wsas.models import WSA
from app.src.waste_transfer.schemas import WasteType


class Vertex:
    def __init__(self, sz : int = 0, cap : int = 0):
        self.sz = sz
        self.cap = cap

class Edge:
    def __init__(self, next: int, length: int):
        self.next = next
        self.length = length

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, id : int, v : Vertex):
        self.vertices[id] = v

    def add_edge(self, id: int, e : Edge):
        if id not in self.edges:
            self.edges[id] = []
        self.edges[id].append(e)

class StorageUpdateQuery:
    def __init__(self, wsa_id : int, waste_type : WasteType, new_size : int):
        self.wsa_id = wsa_id
        self.waste_type = waste_type
        self.new_size = new_size

class Algorithm:
    def __init__(self, graph : Graph):
       self.graph = graph

    def build_queue(self) -> PriorityQueue:
        queue = Queue()
        visited = set()
        res = PriorityQueue()
        queue.put([0, 0])
        while not queue.empty():
            curr_id, curr_dist = queue.get()
            for next in self.graph.edges.get(curr_id, []):
                if next.next not in visited:
                    res.put([curr_dist + next.length, next.next])
                    queue.put([next.next, curr_dist + next.length])
            visited.add(curr_id)

        return res


# a surprise tool that will help me later
'''    
def print_paths(lp : List[Path]):
    for p in lp:
        print([p.id, p.bidirectional, p.length, p.organization_id, p.wsa_start_id, p.wsa_end_id])
    print()

def print_wsas(lw : List[WSA]):
    for w in lw:
        print([w.id, w.name, w.storages])
    print()
'''