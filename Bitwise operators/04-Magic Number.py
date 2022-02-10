# 

"""
Give a number and base, return the magic number

lets assume base = 5 

1 = 0 0 1  ---> 0 * (5^3) + 0 * (5^2) + 1 * (5) ==> 5
2 = 0 1 0  ---> 0 * (5^3) + 1 * (5^2) + 0 * (5) ==> 25
....
"""
def getMagicNumber(n, base):
    ans = 0
    curBase = base
    while n > 0:
        lastDigit = n & 1
        n = n >> 1

        ans += lastDigit * base
        curBase *= base

    return ans


