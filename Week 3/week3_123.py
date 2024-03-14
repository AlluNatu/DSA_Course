import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.pointer = None
    

class LinkedList:
    def __init__(self):
        self.first = None


    def append(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            return
        
        current_node = self.first
        while(current_node.pointer != None):
            current_node = current_node.pointer

        current_node.pointer = new_node
    
    def print(self):
        node_cur = self.first
        while(node_cur):
            if node_cur.pointer is None:
                print(node_cur.data)
            if node_cur.pointer is not None:
                print(node_cur.data, end=" -> ")
            node_cur = node_cur.pointer

    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.first
        finder = 1

        if index == 0 and self.first is None:
            self.first = new_node

        if index == 0 and self.first is not None:
            new_node.pointer = current_node
            self.first = new_node

        while current_node is not None:
            if finder == index:
                new_node.pointer = current_node.pointer
                current_node.pointer = new_node
                break;

            else:
                current_node = current_node.pointer
                finder += 1
        

    def delete(self, index):
        if self.first is None:
            return
        
        current_node = self.first
        finder = 0
        data = current_node.data

        if index == 0 and self.first is not None:
            self.first = current_node.pointer
        
        while current_node is not None:
            if finder == index:
                prev.pointer = current_node.pointer
                current_node = current_node.pointer
                break;

            else:
                prev = current_node
                current_node = current_node.pointer
                if current_node is None:
                    data = None
                else:
                    data = current_node.data
                finder += 1
        return data
    
    def index(self, data):
        current_node = self.first
        index = 0

        if self.first is None:
            return None
        
        while current_node is not None:
            if current_node.data == data:
                return index

            else:
                current_node = current_node.pointer
                index +=1

            if current_node is None:
                return(-1)
        return data

    def swap(self, indexi, indexj):
        datai = self.first.data
        dataj = self.first.data
        counterj = 0
        counteri = 0
        current_node_j = self.first
        current_node_i = self.first

        if indexi == indexj or self.first is None:
            return
    
        while counteri < indexi and current_node_i.pointer is not None:    
            current_node_i = current_node_i.pointer
            datai = current_node_i.data
            counteri += 1

        while counterj < indexj and current_node_j.pointer is not None:
            current_node_j = current_node_j.pointer
            dataj = current_node_j.data
            counterj += 1

        if indexi == counteri and indexj == counterj:
            current_node_i.data = dataj
            current_node_j.data = datai

    def isort(self):
        if self.first is None:
            return
        
        current_node = self.first
        sorted_node = None

        while current_node is not None:
            next_node = current_node.pointer

            if sorted_node is None or current_node.data < sorted_node.data:
                current_node.pointer = sorted_node
                sorted_node = current_node
            else:
                prev = sorted_node
                while prev.pointer is not None and prev.pointer.data <= current_node.data:
                    prev = prev.pointer

                current_node.pointer = prev.pointer
                prev.pointer = current_node

            current_node = next_node

        self.first = sorted_node

                

if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    print(L.index(7))   # 3
    print(L.index(9))   # -1
    L.swap(0,2)
    L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6