class HashLinear:
    def __init__(self, M):
        self.M = M               
        self.T = [None] * M
        return

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return(sum % self.M)

    def insert(self, data):
        index = self.hash(data)
        for i in range(self.M):
            j = (index + i) % self.M
            if self.T[j] == data:
                break;
            if self.T[j] == None:
                self.T[j] = data
                return

    def print(self):
        for i in range(self.M):
            if self.T[i] != None:
                print(str(self.T[i]), end=" ")
            else:
                continue
        print() 

    def delete(self, data):
        for i in range(self.M):
            if self.T[i] == data:
                self.T[i] = None
                break
            else:
                continue





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