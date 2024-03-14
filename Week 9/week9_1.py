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

    def dft(self, n):
        # print(self.matrix)
        self.visited = set()
        self.dft_recursion(n)
        print()

    def dft_recursion(self, n):
        self.visited.add(n)
        print(n, end=" ")
        for i in range(self.size):
            if i not in self.visited and self.matrix[n][i] == 1:
                self.dft_recursion(i)                                   #Numbo uno tapa tehdä
        # for i, a in enumerate(self.matrix[n]):
        #     if i not in self.visited and a == 1:
        #         self.dft_recursion(i)                                 #Numbo tvos tapa tehdä
        return
    
    def bft(self, n):
        j = 0
        queue = []
        queue.append(n)
        while len(queue) > j:
            print(queue[j], end=" ")
            for i in range(len(self.matrix[queue[j]])):
                if self.matrix[queue[j]][i] == 1 and i not in queue:
                    queue.append(i)
            j+=1
        print()
                
            
    def printer(self, N):
        for i in range(N):
            for j in range(N):
                print(f"{self.matrix[i][j]:3d}", end="")
            print()


if __name__ == "__main__":
    graph = Graph(6)
    # graph.printer(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)
    graph.printer(6)
    
        
    # graph.dft(0)           # 0 2 1 5 3 4 
    graph.bft(0)           # 0 2 3 4 1 5 

    # graph.remove(0, 2)
    # graph.remove(2, 5)
    # graph.remove(1, 4)

    # graph.dft(0)           # 0 3 2 1 5 4 
    # graph.bft(0)           # 0 3 4 2 5 1