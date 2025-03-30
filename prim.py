# Essa classe é responsável por encontrar Árvire Geradora Mínima utilizando o
# algoritmo de Prim. De forma resumida, utilizaremos uma fila de prioridade,
# que será a estrutura de dados que nos auxiliará na escolha da próxima aresta
# mais promissora. A partir do nó de início, fazemos com que ele se integre à
# MST, adicionamos todos as suas arestas (evitando arestas que nos levam à um
# nó previamente visitado) à fila de prioridade, e continuamos o ciclo até 
# que o número de arestas seja igual ao número de nós - 1, ou seja, continuamos
# a remover o nó mais barato e que não cause um ciclo até que cheguemos à MST.
import heapq as hq
from typing import List, Tuple
from adjacency_list import AdjacencyList
from graph import Edge

class PrimMST:
    def __init__(self, graph: AdjacencyList):
        self.graph = graph
        self.visited = {node: False for node in graph.items}
        self.pq: List[Edge] = []

    def find_mst(self, start_node: int) -> Tuple[int, List[Edge]]:
        mst_cost = 0
        mst_edges = []

        self.add_edges(start_node)

        while self.pq:
            edge = hq.heappop(self.pq)

            if self.visited[edge.to_node]:
                continue

            mst_edges.append(edge)
            mst_cost += edge.weight
            self.add_edges(edge.to_node)

        return (mst_cost, mst_edges)

    def add_edges(self, node: int):
        self.visited[node] = True
        for edge in self.graph.get_neighbors(node):
            if not self.visited[edge.to_node]:
                hq.heappush(self.pq, edge)

