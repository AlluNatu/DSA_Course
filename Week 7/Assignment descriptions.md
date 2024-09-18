## Assignment 7.1: Car Sales (3 points)

A car shop has cars ***A=[a1,a2,⋯,an]*** (one of each) where ***\ai***  is the price of the car ***i***. Customers ***B=[b1,b2,⋯,bm]*** arrive to the shop. ***bi*** is the price that the customer i can afford. What is the maximum amount of sales that can be made?
For example the shop has cars ***A=[20,10,15,26]*** and there are customers ***B=[11,25,15,9]*** it is possible to make 3 sales.
The first customer (11) gets car that cost 10, The second customer (25) gets the car that cost 20, and the third customer (15) gets the car that cost 15.

Create a function sales(A: list, B: list) in Python which returns the number of possible sales.

Targets:

    The function sales generates the correct solution (2 points).
    The function is Θ(nlogn) or faster (additional 1 point).

Limits:

    1≤n,m≤104 
    1≤ai,bi≤104

A code template with an example program:

    def sales(cars, customers):
        # TODO
    
    if __name__ == "__main__":
        print(sales([20, 10, 15], [11, 25, 15]))                        # 3
        print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
        print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
        print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5


## Assignment 7.2: Subsets (3 points)

A given set that has numbers from 1 to ***N*** in increasing order (1,2,3,4,⋯,N), create a function subsets ***(N: int)*** in Python which produces a list of all possible subsets.

For example when ***N=3*** the subsets are [1], [2], [1,2], [3], [1,3], [2,3] and [1,2,3].

**Note**: The function must return the list of subsets in specific order, The four first generated lists should be:

    subsets(1) -> [[1]]
    subsets(2) -> [[1], [2], [1, 2]]
    subsets(3) -> [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    subsets(4) -> [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

Target: 
  
    The function subsets generates the correct solution (0/3 points).

Limits:
    
    1≤N≤20

A code template with an example program:

    def subsets(n: int) -> list:
        # TODO
    
    
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
