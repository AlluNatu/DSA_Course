class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.size = len(self.matrix)
        self.visited = set()

    def add(self, u , v):
        (self.matrix[v])[u] = 1
        (self.matrix[u])[v] = 1

    def remove(self, u, v):
        (self.matrix[v])[u] = 0
        (self.matrix[u])[v] = 0

    def dft_recursion(self, n):
        self.visited.add(n)
        for i in range(self.size):
            if i not in self.visited and self.matrix[n][i] == 1:
                self.dft_recursion(i)                                   #Numbo uno tapa tehdä
        # for i, a in enumerate(self.matrix[n]):
        #     if i not in self.visited and a == 1:
        #         self.dft_recursion(i)                                 #Numbo tvos tapa tehdä
        return
    
    def subgraphs(self):
        self.visited = set()
        subgraphs = 0
        for v in range(self.size):
            if v not in self.visited:
                subgraphs +=1
                self.dft_recursion(v)
        return subgraphs
            
    def printer(self, N):
        for i in range(N):
            for j in range(N):
                print(f"{self.matrix[i][j]:3d}", end="")
            print()



if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1