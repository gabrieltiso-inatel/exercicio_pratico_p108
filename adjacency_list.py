from typing import Dict, List

from graph import Edge

class AdjacencyList:
    def __init__(self):
        self.items: Dict[int, List[Edge]] = {}

    def add_edge(self, u: int, v: int, cost: int):
        if u not in self.items:
            self.items[u] = []
        if v not in self.items:
            self.items[v] = []
        edge = Edge(u, v, cost)
        self.items[u].append(edge)
        self.items[v].append(Edge(v, u, cost))

    def num_edges(self) -> int:
        return sum(len(edges) for edges in self.items.values()) // 2

    def get_neighbors(self, u: int) -> List[Edge]:
        return self.items.get(u, [])


