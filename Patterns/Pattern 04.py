"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
def Pattern4(n):
    for row in range(1, 2*n):

        TotalCols = row if row <= n else n - (row - n)
        TotalSpaces = n - TotalCols

        print(" " * TotalSpaces, end="")
        for col in range(1, TotalCols + 1):
            print("* ", end="")
        print()


