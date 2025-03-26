# Resolvendo o exercício por meio do algoritmo de Kruskal.
# O algoritmo funciona de forma gulosa. Primeiro obtemos
# a lista de arestas da rede de forma ordenada (crescente).
# A partir disso, o algoritmo começa a iterar sobre as arestas
# e adicioná-las à grupos, todos gerenciados pela estrutura de
# dados `Union-Find`. O algoritmo adiciona diferentes arestas
# à diferentes grupos, e esses grupos vão sendo fundidos em 
# grupos maiores e maiores, até encontrarmos a árvore geradora
# Mínima final, composta por todas as arestas.

# Representa uma aresta na rede
from typing import List, Tuple

from graph import Edge, UndirectedGraph
from union_find import UnionFind

class KruskalMSP:
    def __init__(self, graph: UndirectedGraph):
        self.graph = graph

    # Essa é a função responsável por encontrar a MSP
    def find_msp(self) -> Tuple[int, List[Edge]]:
        sum = 0
        res = []

        edges = self.graph.edges.copy()
        edges.sort()

        n = len(edges) - 1
        uf = UnionFind(n)

        for edge in edges:
            # Se os dois valores estiverem contidos 
            # no mesmo grupo, ignorar (ciclo)
            if uf.contains(edge.from_node, edge.to_node):
                continue

            # Se os dois valores estiverem em grupos
            # diferentes, basta uní-los
            uf.union(edge.from_node, edge.to_node)

            # Adicionar essa aresta à MST, e o custo ao acumulador
            res.append(edge)
            sum += edge.weight

            if uf.size(0) == n:
                break

        return (sum, res)
