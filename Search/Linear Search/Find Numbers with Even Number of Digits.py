import math

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def findNumbers(numbers):
    count = 0
    for num in numbers:
        if even(num):
            count += 1
    return count

def even(val):
    if type(val) == str:
        return even1(val)
    else:
        # return even2(val)
        return optimizedEven(val)

def even1(val):
    return len(str) % 2 == 0

def even2(val):
    if val < 0:
        val *= -1

    digits = 0
    while val > 0:
        digits += 1
        val //= 1
    return digits

def optimizedEven(val):
    digits = int(math.log10(val) + 1)
    return digits % 2 == 0