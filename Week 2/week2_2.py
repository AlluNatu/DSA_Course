def pairs(s):
    counter = 1
    sum = 0
    d = 0
    c = 0
    for i in range(len(s)):

        if s[i] == "1":
            sum = sum + counter*d
            c = sum + c
            d = d + 1
            counter = 1

        if s[i] != "1":
            counter = counter + 1
    return(c)

if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71