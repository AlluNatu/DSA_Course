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
![Figure 1: Breadth-First enumeration for a binary tree. Black: explored, grey: queued to be explored later on (source: wikipedia.org).](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3AAnimated_BFS.gif&psig=AOvVaw097PsALcrDnEKpCXo54cdc&ust=1726743664381000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCIi-gsirzIgDFQAAAAAdAAAAABAE)

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
