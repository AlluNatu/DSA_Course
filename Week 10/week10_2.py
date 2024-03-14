class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.size = len(self.matrix)
        self.visited = set()


    def add(self, v, u, w):
        if u < self.size and v < self.size:
            (self.matrix[v])[u] = w
        else:
            return

    def remove(self, v, u):
        if u < self.size or v < self.size:
            (self.matrix[v])[u] = 0
        else:
            return

    def printer(self, N):
        for i in range(N):
            for j in range(N):
                print(f"{self.matrix[i][j]:3d}", end="")

    def all_paths(self):
        d = [[float('inf')]* self.size for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if (self.matrix[i])[j] != 0:
                    (d[i])[j] = (self.matrix[i])[j]
        for k in range(self.size):  # Compute all k paths
            for i in range(self.size):
                for j in range(self.size):
                    if j == i:
                        d[i][j] = 0
                    if (d[i][k] != float('inf') and
                        d[k][j] != float('inf') and
                        d[i][j] > d[i][k] + d[k][j]):
                        d[i][j] = d[i][k] + d[k][j]
        for i in range(len(d)):
            for j in range(len(d)):
                if (d[i])[j] == float('inf'):
                    (d[i])[j] = -1
        return d



if __name__ == "__main__":

    graph = Graph(6)

    connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
                ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
                ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
                ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

    for u, v, w in connections:
        graph.add(u, v, w)

    A = graph.all_paths()

    for row in A:
        print(row)

    print()
    graph.remove(3, 4)
    graph.remove(1, 0)
    graph.remove(4, 1)

    A = graph.all_paths()
    for row in A:
        print(row)