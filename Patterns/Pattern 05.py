"""
         1
      2  1  2 
   3  2  1  2  3
4  3  2  1  2  3  4

"""
def Pattern5(n):
    for row in range(1, n + 1):
        TotalSpaces = n - row
        print(" "* TotalSpaces, end="")
        for col in reversed(range(1, row + 1)):
            print(col, end="")
        for col in range(2, row + 1):
            print(col, end="")

        print()

