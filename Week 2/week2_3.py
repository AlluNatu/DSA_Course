def split(T):
    remember = T[0]
    count = 0
    sorted_list = sorted(T[1:])
    
    for i in range(len(T) - 1):

        if remember < T[i]:
            remember = T[i]

        if len(sorted_list) > 0 and remember < sorted_list[0]:
            count += 1
    
        sorted_list.pop(0)
    
    return count

if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0