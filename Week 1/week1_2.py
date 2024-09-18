def primes(N):
    A = []
    r = 0
    i = 0
    j = 0
    for j in range(2, N+1):
        prime = True
        for i in range(2, j):
           if j % i == 0:
               prime = False;
               break
        if (prime == True):
            r = r + 1
            A.append(j)
    return r


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
