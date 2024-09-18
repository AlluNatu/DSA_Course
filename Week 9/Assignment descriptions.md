## Assignment 9.1: Creating a Graph (4 points)
A graph has ***n*** vertices but yet no edges between them. Your task is to implement a simple graph structure in Python. On any time, the graph can be modified by creating or removing edges between vertices, or be traversed using depth-first or breadth-first traversals.

Create a class Graph which has following methods (0/4 points):

    __init__(n): initialize a new `Graph` object with n vertices
    add(u, v): creates an undirected edge between vertices u and v
    remove(u, v): removes an edge between vertices u and v
    dft(start): traverses and prints the graph in depth-first order, from start vertex.
    bft(start): traverses and prints the graph in breadth-first order, from start vertex.

Vertices in the graph are labeled from 0 to ***n−1*** as integers (int).

A code template with an example program:

    class Graph:
        # TODO
    
    
    if __name__ == "__main__":
        graph = Graph(6)
        edges = ((0, 2), (0, 4), (2, 1),
                 (2, 3), (2, 5), (3, 0),
                 (3, 5), (4, 5), (5, 1))
        for u, v in edges:
            graph.add(u, v)
            
        graph.dft(0)           # 0 2 1 5 3 4 
        graph.bft(0)           # 0 2 3 4 1 5 
    
        graph.remove(0, 2)
        graph.remove(2, 5)
        graph.remove(1, 4)
    
        graph.dft(0)           # 0 3 2 1 5 4 
        graph.bft(0)           # 0 3 4 2 5 1

## Assignment 9.2: Shortest path (4 points)

A new graph type emerges. Now each edge has a certain weight and a direction. When traversing this graph, it is important to find the least resource consuming path (the smallest sum of weights). This corresponds to finding the shortest path with the weights corresponding to the distances between the nodes.

Create a class Graph which has following methods (0/4 points):

    __init__(n): initialize a new `Graph` object with n vertices
    add(u, v, w): creates a directed edge from vertex u to v with weight w
    remove(u, v): removes an edge from vertex u to v
    shortest_path(start, end): finds the path with the least total weight (the shortest path) from start to end and prints the traversed path including start and end vertices, and -1 if not found.

A code template with an example program:

    class Graph:
        # TODO
    
    
    if __name__ == "__main__":
    
        graph = Graph(10)
        edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
                 (1, 4,  3), (2, 3,  7), (2, 5, 25),
                 (3, 4, 12), (3, 5, 15), (3, 6,  4),
                 (3, 7, 15), (3, 8, 20), (4, 7,  2),
                 (5, 8,  2), (6, 7,  8), (6, 8, 13),
                 (6, 9, 15), (7, 9,  5), (8, 9,  1))
        for u, v, w in edges:
            graph.add(u, v, w)
    
        graph.shortest_path(0, 9)   # 0 2 3 6 7 9
        graph.remove(3, 6)
        graph.remove(5, 6)
        graph.shortest_path(0, 9)   # 0 2 3 5 8 9
