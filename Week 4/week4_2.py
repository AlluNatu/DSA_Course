class HashBucket:
    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.overFlow = []
        self.maxSize = M
        self.T = [[None]*(int(M/N)) for _ in range(N)]
        return

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return(sum % self.N)

    def insert(self, data):
        index = self.hash(data)
        for i in range(len(self.T[index])):
            if self.T[index][i] == data:
                return

            if self.T[index][i] == None:
                self.T[index][i] = data
                return
            
        if data not in self.overFlow and len(self.overFlow) <= self.maxSize:
            self.overFlow.append(data)

    def print(self):
        for i in range(self.N):
            for j in range(len(self.T[i])):
                if self.T[i][j] != None:
                    print(str(self.T[i][j]), end=" ")
        for i in self.overFlow:
            if i != None:
                print(i, end=" ")
        print()

    def delete(self, data):
        for i in range(self.N):
            for j in range(len(self.T[i])):
                if self.T[i][j] == data:
                    self.T[i][j] = None
                    break
        
        if data in self.overFlow:
            self.overFlow.remove(data)





if __name__ == "__main__":
    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    table.print()