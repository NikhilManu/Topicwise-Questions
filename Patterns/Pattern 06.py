"""
         1
      2  1  2 
   3  2  1  2  3
4  3  2  1  2  3  4
   3  2  1  2  3
      2  1  2 
         1

"""
def Pattern6(n):
    for row in range(1, 2 * n):
        TotalCols = 2 * n - row if row >= n else row
        TotalSpaces = n - TotalCols

        print(" "* TotalSpaces, end="")
        for col in reversed(range(1, TotalCols + 1)):
            print(col, end="")
        for col in range(2, TotalCols + 1):
            print(col, end="")

        print()
