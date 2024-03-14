def subsets(n: int) -> list:
    list = []
    for x in range(1, n+1):
        list.append([x])
        for y in range(len(list)-1):
            list.append(list[y] + [x])
    
    return list



if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]