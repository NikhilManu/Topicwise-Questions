"""
*****
****
***
**
*
"""
def Pattern2(n):
    for row in range(1, n+1):
        for col in range(row, n+1):
            print("*", end="")
        print()

