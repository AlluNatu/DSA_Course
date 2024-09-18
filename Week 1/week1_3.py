def triangle(a, b, c):
        factor = False
        if (a + b > c) and (c + a > b) and (b + c > a):
            factor = True
        return factor


    if __name__ == "__main__":
        print(triangle(3, 5, 4))    # True
        print(triangle(-1, 2, 3))   # False
        print(triangle(5, 9, 14))   # False
        print(triangle(30, 12, 29)) # True

