## Assignment 10.1 Sub-Graphs (2 points)
Your task is to implement a graph structure in Python. On any time, the graph can be modified by creating or removing connection between two nodes. If two nodes can be reached by built connections, they belong to the same sub-graph. On any time, the graph can determine how many sub-graphs it contains.

Create a class Graph which has following methods:

    __init__(n): initialize a new Graph object with n vertices
    add(u, v): creates an undirected edge between vertex u and v
    remove(u, v): removes an edge between vertex u and v
    subgraphs(): returns the number of sub-graphs in the whole graph

Nodes in the graph are labeled from 0 to ***n−1*** as integers (int).

A code template with an example program:

    class Graph:
        # TODO
    
    
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
    
## Assignment 10.2: All Paths (3 points)

Your task is to implement a graph structure in Python. On any time, the graph can be modified by creating or removing connection of certain weight between two nodes. Additionally, the graph can display ***n×n*** matrix of shortest paths (least weight) between each node.

Create a class Graph which has following methods:

    __init__(n): initialize a new Graph object with n vertices
    add(u, v, w): creates a directed edge from vertex u to v with weight (distance) w
    remove(u, v): removes an edge from vertex u to v
    all_paths(): returns a n×n
    matrix (list of lists) of all shortest paths between vertices, nonexistent paths are given value of -1 Nodes in the graph are labeled from 0 to n−1 as integers (int).

A code template with an example program:
    
    class Graph:
        # TODO
    
    
    if __name__ == "__main__":
        graph = Graph(6)
        edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                 (2, 3, 1), (2, 5, 2), (3, 0, 6),
                 (3, 5, 2), (4, 5, 1), (5, 1, 6))
        for u, v, w in edges:
            graph.add(u, v, w)
    
        M = graph.all_paths()
        for weights in M:
            for weight in weights:
                print(f"{weight:3d}", end="")
            print()
        #  0 12  7  8  9  9
        # -1  0 -1 -1 -1 -1
        #  7  5  0  1 16  2
        #  6  8 13  0 15  2
        # -1  7 -1 -1  0  1
        # -1  6 -1 -1 -1  0

## Assignment 10.3 Minimal Cost Spanning Tree (3 points)

Your task is to implement a graph structure in Python. On any time, the graph can be modified by creating or removing connection of certain weight between two nodes. Additionally, it is possible to determine what is the minimal cost spanning tree and calculate its total weight.

Create a class Graph which has following methods:

    __init__(n): initialize a new Graph object with n vertices
    add(u, v, w): creates an undirected edge between vertex u and v with weight w
    remove(u, v): removes an edge between vertex u and v
    min_expense(): computes a total weight (the sum of weights) of minimal cost spanning tree of the graph.

A code template with an example program:

    class Graph:
        # TODO
    
    
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
