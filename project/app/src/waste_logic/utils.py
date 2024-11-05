from queue import Queue, PriorityQueue


class Vertex:
    def __init__(self, sz: int = 0, cap: int = 0):
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

    def add_vertex(self, id: int, v: Vertex):
        self.vertices[id] = v

    def add_edge(self, id: int, e: Edge):
        if id not in self.edges:
            self.edges[id] = []
        self.edges[id].append(e)


class StorageUpdateQuery:
    def __init__(self, wsa_id: int, new_size: int):
        self.wsa_id = wsa_id
        self.new_size = new_size


class Algorithm:
    def __init__(self, graph: Graph):
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

    def generate_queries(self, transfer_amount: int, queue: PriorityQueue):
        left: int = transfer_amount
        res = Queue()
        while (left > 0) and (not queue.empty()):
            _, wsa_id = queue.get()
            v: Vertex = self.graph.vertices.get(wsa_id, None)
            if (v is not None) and (v.cap > 0):
                dif = v.cap - v.sz
                if dif <= left:
                    res.put(StorageUpdateQuery(wsa_id, v.cap))
                    left -= dif
                else:
                    res.put(StorageUpdateQuery(wsa_id, v.sz + left))
                    left = 0
        return [left, res]
