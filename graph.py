from typing import Self, List

class Edge:
    def __init__(self, from_node: int, to_node: int, weight: int):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __lt__(self, other: Self):
        return self.weight < other.weight

    def __str__(self):
        return f"[Edge: from = {self.from_node}, to = {self.to_node}, weight = {self.weight}"

# Representa o conjunto de arestas. O valor (id) 
# do nó já está contido na aresta.
class UndirectedGraph: 
    def __init__(self):
        self.edges: List[Edge] = []

    def add_undirected_edge(self, from_node: int, to_node: int, weight: int):
        # Uma rede não-direcionada conecta os nós na ida e na volta
        self.edges.append(Edge(from_node, to_node, weight))
        self.edges.append(Edge(to_node, from_node, weight))
