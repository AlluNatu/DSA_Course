# Week 1
### Assignment 1.1: Insertion Sort (3 points)

Following pseudo code sorts an array of integers. Command swap switches values of two variables.

    function isort(A)
        for i = 1 to size(A)-1
            j = i-1
            while (j >= 0) and (A[j] > A[j+1])
                swap(A[j], A[j+1])
                j = j-1
        return

Create the following function in Python:

    isort(A: list): sorts a given list of integers. Implement the given pseudo code to this function.

Limits:

    the maximum length of the list is 103
    each integer is between 1...103

A code template with an example program:

    def isort(A):
        # TODO

    if __name__ == "__main__": 
        A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
        isort(A)
        print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


## Assignment 1.2 Prime Numbers (3 points)

For the background read the first paragraph of this article: https://en.wikipedia.org/wiki/Prime_number

Given a number N how many prime numbers are less or equal to N? For example if N=7 there are four prime numbers: 2, 3, 5 and 7 (note that 1 is not a prime number).

Create the following function in Python:

    primes(N: int): returns the numbers of primes that are less or equal to N

Limits:

    1≤N≤105

A code template with an example program:

    def primes(N):
        # TODO
        
    if __name__ == "__main__":
        print(primes(7))    # 4
        print(primes(15))   # 6
        print(primes(50))   # 15

## Assignment 1.3: Is it a Triangle? (3 points)

Three integers a, b and c

presents the side lenghts of a triangle. Can you build any triangle from those three sides?

For example:

    sides 3, 4 and 5 makes a right angle
    triangle sides 5, 5 and 3 makes an isosceles triangle
    sides 7, 3 and 3 doesn't make a triangle sides 4, 3 and −1 doesn't make a triangle

Create the following function in Python:

    triangle(a: int, b: int, c: int): returns a boolean True if triangle can be built, False if not

A code template with an example program:

    def triangle(a, b, c):
        # TODO
        
    if __name__ == "__main__":
        print(triangle(3, 5, 4))    # True
        print(triangle(-1, 2, 3))   # False
        print(triangle(5, 9, 14))   # False
        print(triangle(30, 12, 29)) # True

# Week 2
## Assignment 2.1: Changes (3 points)

An array of n number of integers must be modified so that no two consecutive integers are equal. The new value can be chosen arbitrarily. What is the minimum number of required changes?
For Example array [1,1,2,2,2] requires 2 changes. Changed array can be e.g. [1,3,2,3,2].

Create the following function in Python:

        changes(A: list): returns the minimum number of required changes

Limits:

        1≤n≤106
        each integer is between 1...103

Target: 
  
    Algorithm performs in Θ(n) time.

A code template with an example program:

    def changes(A):
        # TODO
    
    
    if __name__ == "__main__":
        print(changes([1, 1, 2, 2, 2]))     # 2
        print(changes([1, 2, 3, 4, 5]))     # 0
        print(changes([1, 1, 1, 1, 1]))     # 2

## Assignment 2.2: Bit Pairs (3 points)

We are given a bit string which each character is either 0 or 1. Count the sum of each distance of bit pairs where both bits are 1.

For example a bit string 100101 has following distances

        100101 (3)
        100101 (5)
        100101 (2)

Therefore the sum of distances is 3+5+2=10.

Create the following function in Python:

        pairs(s: str): returns the sum of distances

Limits: 

    the maximum length of the bit string is 105

Target:

    Algorithm performs in Θ(n) time.

A code template with an example program:

    def pairs(s):
        # TODO
    
    if __name__ == "__main__":
        print(pairs("100101"))          # 10
        print(pairs("101"))             # 2
        print(pairs("100100111001"))    # 71

## Assignment 2.3: Split Lists (3 points)

An array of n number of integers must be split in two sub arrays so that every integer of left sub array are smaller than every integer of right sub array. In how many points the array can be split in half?

For example array [2,1,2,5,7,6,9]

can be split in 3 ways:

    [2,1,2] and [5,7,6,9]
    [2,1,2,5] and [7,6,9]
    [2,1,2,5,7,6] and [9]

Create following function(s) in Python:

        split(A: list): returns the number of possible splits

Limits:

    1≤n≤105
    each integer is between 1...103

Target:

    Algorithm performs in Θ(n) time.

A code template with an example program:
    
    def split(T):
        # TODO
    
    
    if __name__ == "__main__":
        print(split([1,2,3,4,5]))       # 4
        print(split([5,4,3,2,1]))       # 0
        print(split([2,1,2,5,7,6,9]))   # 3
        print(split([1,2,3,1]))         # 0

# Week 3
## Assignment 3.1: Linked List (4 points)

Implement the linked list data structure in Python. Create a class Node which stores the data (integer) and link to another Node object in the list. Create an additional class LinkedList which maintains the linked list created by Node objects. 
You can implement your linked list with or without header and trailer nodes.

Class LinkedList must contain following methods:

    append(data: object): inserts data to the end of the linked list
    insert(data: object, i: int): inserts data to the index i.
    delete(i: int): deletes and returns data from a node from the position indicated by the index i.
    print(): prints the content of linked list (format: node1 -> node2 -> node3).

A code template with an example program:

    class Node:
        # TODO
        
    
    class LinkedList:
        # TODO
    
    
    if __name__ == "__main__":
        L = LinkedList()
        L.append(1)
        L.append(3)
        L.print()           # 1 -> 3
        L.insert(10, 1)
        L.insert(15, 0)
        L.print()           # 15 -> 1 -> 10 -> 3
        L.delete(0)
        L.print()           # 1 -> 10 -> 3

## Assignment 3.2: Indices and Swapping (2 points)

Implement two new methods to your LinkedList class:

    index(data: object): returns the index where data is stored in linked list, returns −1 if not found.
    swap(i: int, j: int): swaps two nodes in locations i and j, returns without changes if indices are invalid.

A code template with an example program:

    if __name__ == "__main__":
        L = LinkedList()
        for num in (3, 5, 2, 7, 8, 10, 6):
            L.append(num)
        L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
        print(L.index(7))   # 3
        print(L.index(9))   # -1
        L.swap(1, 4)
        L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
        L.swap(2, 0)
        L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6


## Assignment 3.3: Insertion Sort (2 points)

Consider week’s 1 assignment 1.1: Insertion Sort.
Implement a new method isort to your LinkedList class. The method sorts the linked list in ascending order using insertion sort.

A code template with an example program:

    if __name__ == "__main__":
        L = LinkedList()
        for num in (3, 5, 2, 7, 8, 10, 6):
            L.append(num)
        L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
        L.isort()
        L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10

# Week 4
Both assignments are related to fixed sized hash tables. The hash tables store string (str) values. The hash value (slot) is calculated with the following hash function for strings:

    procedure hash(data):
        sum = 0
        for i = 0 to N-1 do
            sum += ascii(data[i])
        return sum % X
where N is the length of the string (data), % is the symbol for the mod operation and X is a parameter of the hash table. The ascii value of a character can be calculated with the function ord in Python.


## Assignment 4.1: Linear Probing (4 points)

Implement a fixed sized hash table in Python that uses linear probing for collision resolution. Create a class HashLinear which has the table size M as a input value when a object is created. The class has following methods:

    insert(data: str): inserts data into the hash table, ignores duplicates
    delete(data: str): removes data from the hash table
    print(): prints the content of the hash table (the data string in each slot separated with a space; skip empty slots; see the example below)

For hashing use ***X***=***M***.
A code template with an example program (the hash table has the size of ***M=8***):

    class HashLinear:
        # TODO
    
    
    if __name__ == "__main__":
        table = HashLinear(8)
        table.insert("BM40A1500")
        table.insert("fOo")
        table.insert("123")
        table.insert("Bar1")
        table.insert("10aaaa1")
        table.insert("BM40A1500")
        table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
        table.delete("fOo")
        table.delete("Some arbitary string which is not in the table")
        table.delete("123")
        table.print()   # 10aaaa1 BM40A1500 Bar1


## Assignment 4.2: Bucket Hashing (4 points)

Implement a fixed sized hash table in Python that uses bucket hashing for collision resolution. Create a class HashBucket which has the table size (M) and number of equal sized buckets (B) as the input values when a object is created. The hash table has a overflow array of size (M). The class has the following methods:

    insert(data): inserts data in the hash table, ignores duplicates
    delete(data): removes data from the hash table
    print(): prints the content of the hash table and the overflow array (the data string in each slot followed by the data in the overflow array; slots separated with a space and empty slots skipped; see the example below)

For hashing use (***X = B***). Filling the buckets starts from the top and overflow values are appended to the end of the overflow array.
A code template with an example program (the hash table has the size of (M=8) and has (B=4) buckets):

    class HashBucket:
        # TODO
    
    
    if __name__ == "__main__":
        table = HashBucket(8, 4)
        table.insert("BM40A1500")
        table.insert("fOo")
        table.insert("123")
        table.insert("Bar1")
        table.insert("10aaaa1")
        table.insert("BM40A1500")
        table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
        table.delete("fOo")
        table.delete("Some arbitary string which is not in the table")
        table.delete("123")
        table.print()   # BM40A1500 Bar1 10aaaa1

  # Week 5
## Assignment 5.1: Binary Search Tree (3 points)

Implement a binary seach tree in Python. The tree stores integers (int) only.

Create following classes:

    Node: stores the integer value (int) and links to its left and right child
    BST: maintains the binary search tree built using Node objects.

Create following methods for class BTS:

    insert(key: int): inserts a key to the search tree, ignores duplicates.
    search(key: int): searches key from the search tree and returns boolean True if found, False otherwise.
    preorder(): prints the content of the search tree in preorder.
    remove(key: int): removes key from the search tree, maintains the BST property. Implement remove using the maximum node principle.

A code template with an example program:

    class Node:
        # TODO
    
    
    class BST:
        # TODO
    
    
    if __name__ == "__main__":
        Tree = BST()
        keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]
    
        for key in keys:
            Tree.insert(key)
    
        Tree.preorder()         # 5 1 3 2 4 9 7 6
     
        print(Tree.search(6))   # True
        print(Tree.search(8))   # False
        
        Tree.remove(1)
        Tree.preorder()         # 5 3 2 4 9 7 6
        Tree.remove(9)
        Tree.preorder()         # 5 3 2 4 7 6 
        Tree.remove(3)
        Tree.preorder()         # 5 2 4 7 6


## Assignment 5.2: More Traversals (3 points)

Update your class BST with three new traversal methods:

    postorder(): prints the content of the search tree in postorder.
    inorder(): prints the content of the search tree in inorder.
    breadthfirst(): prints the content of the search tree in breadth-first-order.

Breadth-First enumeration presents the nodes of the search tree level by level (or depth), unlike other impemented methods which traverses the left subtree first before the right subtree.

![Figure 1: Breadth-First enumeration for a binary tree. Black: explored, grey: queued to be explored later on (source: wikipedia.org).](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

An example program:

    if __name__ == "__main__":
        Tree = BST()
        keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]
    
        for key in keys:
            Tree.insert(key)
       
        Tree.postorder()        # 2 4 3 1 6 7 9 5 
        Tree.inorder()          # 1 2 3 4 5 6 7 9  
        Tree.breadthfirst()     # 5 1 9 3 7 2 4 6



## Assignment 5.3: Mirroring The BST (3 points)

Implement a new method mirror() to your class BST. The method mirrors the search tree along the root node, i.e. each nodes’ left and right child nodes will swap places.
While traversal methods can remain as they are, update methods insert, search and remove so that the BST property remains whether the tree is mirrored or not.

An example program:

    if __name__ == "__main__":
        Tree = BST()
        keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]
    
        for key in keys:
            Tree.insert(key)
    
        Tree.preorder()         # 5 1 3 2 4 9 7 6
        Tree.mirror()
        Tree.preorder()         # 5 9 7 6 1 3 4 2 
    
        Tree.insert(8)
        Tree.remove(3)
        print(Tree.search(2))   # True
        Tree.preorder()         # 5 9 7 8 6 1 2 4
        Tree.mirror()
        Tree.preorder()         # 5 1 2 4 9 7 6 8

  # Week 6

  ## Assignment 6.1: The AVL Tree (4 points)

Implement a AVL tree data structure in Python. Create following classes:

    AVLNode: stores a value (int) and links to its left and right child nodes.
    AVL: stores the tree structure built using AVLNode objects and maintains the AVL-tree property

You are free to use all the code presented in the AVL Tree example written in Python. Finalize the class AVL by creating following methods:

    left_rotation(node: AVLNode): symmetrical to right_rotation
    right_left_rotation(node: AVLNode): symmetrical to left_right_rotation
    preorder(): enumerates the keys and their balance values in preorder
    the format: key1:balance1 key2:balance2 key3:balance3

Finally, finalize the method insert_help so that it functions properly.

A code template with an example program:

    class AVLNode:
        # TODO
    
    
    class AVL:
        # TODO
    
    
    if __name__ == "__main__":
        Tree = AVL()
        for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
            Tree.insert(key)
        Tree.preorder()     # 9;-1 4;0 2;0 1;0 3;0 6;0 5;0 7;0 10;1 11;0


## Assignment 6.2: The Min Heap (4 points)

Implement the min heap structure in Python. Create class MinHeap which takes a list of numbers (int) as an input value and forms the heap from them. The class must have following methods:

    __init__(A: list): initializer, forms the heap from a list A using the efficient method
    push(key: int): inserts a new key to the heap while maintaining the min heap property.
    pop(): removes the smallest key from the heap and returns its value.
    print(): prints the heap in breadth-first order
    the format: key values separated by spaces (e.g. 1 2 3 4).

Make sure that the heap always maintains the min heap property. The best practice is to store the heap structure in a list where a key in index ***i*** has a left child at index ***2i+1*** has a right child at index ***2i+2*** has its parent at index (rounds down to the nearest integer)

    A code template with an example program:
    
    class MinHeap:
        # TODO
    
    
    if __name__ == "__main__":
        heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
        heap.print()        # 1 4 2 5 8 6 3 
        print(heap.pop())   # 1
        heap.push(9)
        heap.print()        # 2 4 3 5 8 6 9

# Week 7
## Assignment 7.1: Car Sales (3 points)

A car shop has cars ***A=[a1,a2,⋯,an]*** (one of each) where ***\ai***  is the price of the car ***i***. Customers ***B=[b1,b2,⋯,bm]*** arrive to the shop. ***bi*** is the price that the customer i can afford. What is the maximum amount of sales that can be made?
For example the shop has cars ***A=[20,10,15,26]*** and there are customers ***B=[11,25,15,9]*** it is possible to make 3 sales.
The first customer (11) gets car that cost 10, The second customer (25) gets the car that cost 20, and the third customer (15) gets the car that cost 15.

Create a function sales(A: list, B: list) in Python which returns the number of possible sales.

Targets:

    The function sales generates the correct solution (2 points).
    The function is Θ(nlogn) or faster (additional 1 point).

Limits:

    1≤n,m≤104 
    1≤ai,bi≤104

A code template with an example program:

    def sales(cars, customers):
        # TODO
    
    if __name__ == "__main__":
        print(sales([20, 10, 15], [11, 25, 15]))                        # 3
        print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
        print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
        print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5


## Assignment 7.2: Subsets (3 points)

A given set that has numbers from 1 to ***N*** in increasing order (1,2,3,4,⋯,N), create a function subsets ***(N: int)*** in Python which produces a list of all possible subsets.

For example when ***N=3*** the subsets are [1], [2], [1,2], [3], [1,3], [2,3] and [1,2,3].

**Note**: The function must return the list of subsets in specific order, The four first generated lists should be:

    subsets(1) -> [[1]]
    subsets(2) -> [[1], [2], [1, 2]]
    subsets(3) -> [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    subsets(4) -> [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

Target: 
  
    The function subsets generates the correct solution (0/3 points).

Limits:
    
    1≤N≤20

A code template with an example program:

    def subsets(n: int) -> list:
        # TODO
    
    
    if __name__ == "__main__":
        print(subsets(1))   # [[1]]
        print(subsets(2))   # [[1], [2], [1, 2]]
        print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                            #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                            #  [2, 3, 4], [1, 2, 3, 4]]
        S = subsets(10)
        print(S[95])    # [6, 7]
        print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
        print(S[826])   # [1, 2, 4, 5, 6, 9, 10]

# Week 8
## Assignment 8.1: Jumps (4 points)

You are playing a game which has ***n*** levels. You start from the level 0 and your goal is to reach the level n by jumping from a level to another. From every level you're able to jump only to ***a*** or ***b*** levels higher at a time. In how many different ways can you complete the game?

e.g.: let n=8, a=2 and b=3, there are 4 different ways to pass the game.

    0→2→4→6→8
    0→2→5→8
    0→3→5→8
    0→3→6→8

Create a function jumps(n: int, a: int, b: int) in Python which returns the number of all possible ways to complete the game.

Limits (you can assume that):

    n≤10000
    1≤a<b≤n

Targets:

    correct solution: 2 points
    performs in Θ(n) time: +2 points (the solution must be correct)

A code template with an example program:

    def jumps(n, a, b):
        # TODO
    
    
    if __name__ == "__main__":
        print(jumps(4, 1, 2)) # 5
        print(jumps(8, 2, 3)) # 4
        print(jumps(11, 6, 7)) # 0
        print(jumps(30, 3, 5)) # 58
        print(jumps(100, 4, 5)) # 1167937

## Assignment 8.2: All Sums (4 points)

***A*** is a list consisting of ***n*** integers. How many different sums can be generated with the given integers?

For example:

    list [1,2,3] has 6 possible sums: 1, 2, 3, 4, 5 and 6
    list [2,2,3] has 5 possible sums: 2, 3, 4, 5 and 7

Create a function sums(A: list) in Python which computes the number of all different sums.

Limits (you can assume that): 

    1≤n,ai≤100

Targets

    correct solution: 2 points
    performs in Θ(n3) time: +2 points (the solution be must correct)

A code template with an example program:

    def sums(items):
        # TODO
    
    
    if __name__ == "__main__":
        print(sums([1, 2, 3]))                  # 6
        print(sums([2, 2, 3]))                  # 5
        print(sums([1, 3, 5, 1, 3, 5]))         # 18
        print(sums([1, 15, 5, 23, 100, 55, 2])) # 121

# Week 9
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
        
# Week 10
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
