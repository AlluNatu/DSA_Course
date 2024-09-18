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
