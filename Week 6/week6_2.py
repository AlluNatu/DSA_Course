class MinHeap:
    def __init__(self, list):
        self.list = list
        self.heapify(self.list)

    def heapify(self, list):
        while True:
            checker = 0
            for index in range((len(self.list)// 2) - 1, -1, -1):
                parent_node_value = list[index]
                if len(self.list)-1 >= index*2 + 2:
                    if parent_node_value > self.list[index*2+1] or parent_node_value > self.list[index*2+2]:
                        checker = 1
                        if self.list[index*2+1] < self.list[index*2+2]:
                            self.list[index] = self.list[index*2+1]
                            self.list[index*2+1] = parent_node_value
                        else:
                            self.list[index] = self.list[index*2+2]
                            self.list[index*2+2] = parent_node_value
                elif len(self.list)-1 >= index*2+1:
                    if parent_node_value > self.list[index*2+1]:
                        checker = 1
                        self.list[index] = self.list[index*2+1]
                        self.list[index*2+1] = parent_node_value
            if checker == 0:
                break

    def print(self):
        list = self.list
        for index in list:
            print(index, end=" ")
        print()

    def pop(self):
        list = self.list
        if len(list) > 0:
            popped = list[0]
            last_value = list.pop()
            if len(list) > 0:
                list[0] = last_value
                self.heapify(list)
                self.heapify(list)
            return popped
        else:
            return

    def push(self, value):
        list = self.list
        list.append(value)
        index = len(list) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if list[index] < list[parent_index]:
                temp = list[index]
                list[index] = list[parent_index]
                list[parent_index] = temp
                index = parent_index
            else:
                break

               



if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3 
    print(heap.pop())   # 1
    heap.print()  
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9