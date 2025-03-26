class UnionFind:
    def __init__(self, num_items: int):
        self.num_items = num_items
        self.sizes = [1] * num_items
        self.ids = [i for i in range(0, num_items)]

    # Para encontrar o grupo ao qual o nó `p` pertence,
    # basta encontrar a raíz do grupo. Ao mesmo tempo, 
    # Depois de encontrar a raiz, basta aplicar a compressão
    # de caminhos para otimizar o algoritmo.
    def find(self, p: int):
        root = p
        while root != self.ids[root]:
            root = self.ids[root]

        # Subimos a cadeia de pais do nó 
        # p, e alteramos seu id para apontar
        # para a raiz (root)
        while p != root:
            next = self.ids[p]
            self.ids[p] = root
            p = next

        return root

    def contains(self, p: int, q: int):
        return self.find(p) == self.find(q)

    # A união consiste em obter os grupos 
    # aos quais pertencem p e q. Para unir,
    # vamos fazer o grupo de tamanho menor
    # se juntar ao grupo de tamanho maior
    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.size(p_root) < self.size(q_root):
            self.ids[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.ids[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]

    # O tamanho se refere ao grupo. Por isso referenciamos sizes
    # com o índice de self.find(p), pois este contém minha raíz
    def size(self, p: int):
        return self.sizes[self.find(p)]

