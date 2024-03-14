class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.size = len(self.matrix)
        self.visited = set()


    def add(self, v, u, w):
        if u < self.size and v < self.size:
            (self.matrix[v])[u] = w
            (self.matrix[u])[v] = w
        else:
            return

    def remove(self, v, u):
        if u < self.size or v < self.size:
            (self.matrix[v])[u] = 0
            (self.matrix[u])[v] = 0
        else:
            return

    def printer(self, N):
        for i in range(N):
            for j in range(N):
                print(f"{self.matrix[i][j]:3d}", end="")
            print()
    
    def min_expense(self):
        dist = [float('inf')]*self.size
        prev = [None]*self.size
        queue =[i for i in range(self.size)]
        dist[0] = 0

        while queue:
            u = self.minVertex(queue, dist)
            queue.remove(u)

            for v in range(self.size):
                if (self.matrix[u])[v] != 0 and v in queue:
                    alt = (self.matrix[u])[v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
        
        size = 0
        print(dist)
        for i in dist:
            if i == float('inf'):
                continue
            else:
                size = size + i
        return size



    def minVertex(self, queue, dist):
        minimum = None
        for i in (queue):
            if minimum == None:
                minimum = i
            if dist[i] < dist[minimum]:
                minimum = i
        return minimum


if __name__ == "__main__":

    graph = Graph(6)
    edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
             (2, 3, 1), (2, 5, 2), (3, 0, 6),
             (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in edges:
        graph.add(u, v, w)

    print(graph.min_expense())  # 15

    graph.remove(2, 3)

    print(graph.min_expense())  # 16