class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.size = len(self.matrix)
        self.visited = set()


    def add(self, v, u, w):
        (self.matrix[v])[u] = w

    def remove(self, v, u):
        (self.matrix[v])[u] = 0

    def printer(self, N):
        for i in range(N):
            for j in range(N):
                print(f"{self.matrix[i][j]:3d}", end="")
            print()
    
    def shortest_path(self, source, destination):
        dist = [float('inf')]*self.size
        prev = [None]*self.size
        queue =[i for i in range(self.size)]
        dist[source] = 0

        while queue:
            u = self.minVertex(queue, dist)
            queue.remove(u)

            for v in range(self.size):
                if (self.matrix[u])[v] != 0:
                    alt = dist[u] + (self.matrix[u])[v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
        path = []
        adder = destination
        while adder != None:
            path.append(adder)
            adder = prev[adder]
        path.reverse()
        if path[0] == destination:
            print(-1)
        else:
            for i in path:
                print(i, end=" ")
            print()



    def minVertex(self, queue, dist):
        minimum = None
        for i in (queue):
            if minimum == None:
                minimum = i
            if dist[i] < dist[minimum]:
                minimum = i
        return minimum


if __name__ == "__main__":

    graph = Graph(8)

connections = ((0, 6, 15), (0, 7, 13), (1, 0, 12),
               (1, 2, 19), (2, 3, 20), (3, 6, 24),
               (4, 3, 29), (5, 4, 17), (5, 6, 14), 
               (6, 1, 16), (6, 2, 22), (6, 4, 19),
               (7, 5, 29), (7, 6, 11), (7, 2, 25))

for u, v, w in connections:
    graph.add(u, v, w)

graph.shortest_path(0, 4)
graph.shortest_path(1, 5)
graph.shortest_path(7, 3)

graph.remove(1, 0)
graph.remove(7, 6)
graph.remove(5, 4)
graph.remove(6, 1)

graph.shortest_path(1, 6)
graph.shortest_path(1, 5)
graph.shortest_path(7, 3)
graph.shortest_path(3, 4)