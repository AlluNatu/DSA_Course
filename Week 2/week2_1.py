def changes(A):
    c = 0
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            A[i+1]+=123
            c+=1

    return(c)




if __name__ == "__main__":
    print(changes([3, 3, 5, 1, 4, 2, 1, 2, 1]))