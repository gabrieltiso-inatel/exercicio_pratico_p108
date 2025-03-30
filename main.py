from adjacency_list import AdjacencyList
from graph import UndirectedGraph
from kruskal import KruskalMSP
from prim import PrimMST

def main():
   graph = UndirectedGraph() 
   graph.add_undirected_edge(0, 1, 7)
   graph.add_undirected_edge(0, 2, 6)
   graph.add_undirected_edge(1, 2, 4)
   graph.add_undirected_edge(1, 3, 4)
   graph.add_undirected_edge(1, 4, 3)
   graph.add_undirected_edge(2, 3, 4)
   graph.add_undirected_edge(2, 4, 3)
   graph.add_undirected_edge(3, 4, 3)
   graph.add_undirected_edge(3, 5, 7)
   graph.add_undirected_edge(4, 5, 2)

   kruskal = KruskalMSP(graph)
   cost, path = kruskal.find_mst()

   print("====== KRUSKAL =====")
   print(f"Minimal cost: {cost}")
   print("Edges:")
   for edge in path:
       print(edge)

   graph = AdjacencyList()
   graph.add_edge(0, 1, 7)
   graph.add_edge(0, 2, 6)
   graph.add_edge(1, 2, 4)
   graph.add_edge(1, 3, 4)
   graph.add_edge(1, 4, 3)
   graph.add_edge(2, 3, 4)
   graph.add_edge(2, 4, 3)
   graph.add_edge(3, 4, 3)
   graph.add_edge(3, 5, 7)
   graph.add_edge(4, 5, 2)

   prim = PrimMST(graph)
   cost, path = prim.find_mst(0)

   print("====== PRIM =====")
   print(f"Minimal cost: {cost}")
   print("Edges:")
   for edge in path:
       print(edge)

if __name__ == "__main__":
    main()
