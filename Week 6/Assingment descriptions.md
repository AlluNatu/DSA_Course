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
