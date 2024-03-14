def sums(items):
    meow = set()
    for j in items:
        meow_copy = {j}
        for i in meow:
            meow_copy.add(j+i)
        meow.update(meow_copy)
    return len(meow)

if __name__ == "__main__":
        print(sums([1, 2, 3]))                  # 6
        print(sums([2, 2, 3]))                  # 5
        print(sums([1, 3, 5, 1, 3, 5]))         # 18
        print(sums([1, 15, 5, 23, 100, 55, 2])) # 121