# https://leetcode.com/problems/single-number

# Time O(N) | Space O(1)
def SingleNumber(nums):
    x = 0
    for num in nums:
        x ^= num
    return x


# Say every number is appearing odd time and only one number is once
"""
Here we have to find the count of set Bit of each pos and modulo it by the odd number to get the answer

arr = [2, 2, 3, 2, 7, 7, 7]

--> 0 1 0
--> 0 1 0
--> 0 1 1
--> 0 1 0
--> 1 1 1
--> 1 1 1
--> 1 1 1
-------------
--> 3 7 4

take modulo with 3 --> 0 1 1 --> 3
"""