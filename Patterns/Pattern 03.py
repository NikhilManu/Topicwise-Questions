"""
*
* *
* * *
* * * *
* * *
* *
*
"""
def Pattern3(n):
    for row in range(1, 2*n): # 2*n - 1 rows are there
        c = row if row <= n else n - (row - n)
        for col in range(1, c + 1):
            print("*", end="")
        print()

Pattern3(4)