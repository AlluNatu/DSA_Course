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
