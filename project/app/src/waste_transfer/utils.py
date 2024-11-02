
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
        self.edges[id] = e