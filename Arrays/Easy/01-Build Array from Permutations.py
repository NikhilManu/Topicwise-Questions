# https://leetcode.com/problems/build-array-from-permutation/

# Solution 1
# Time - O(N) | Space O(N)
def buildArray(nums):
    return [nums[num] for num in nums]

# Solution 2
# TIme O(N) | Space O(1)
def buildArray(nums):
    n = len(nums)
    for i in range(n):
        nums[i] = nums[i] + (n * (nums[nums[i]] % n)) # % n  is used if any changes had happened to the value during the previous iterations
        
    for i in range(n):
        nums[i] //= n # using eqn for b
        
    return nums

"""
let nums = [0, 2, 1, 5, 3, 4]  -->  result = [0, 1, 2, 4, 5, 3]

At any we have two numbers on hand ..ie.. a = nums[i] and b = nums[nums[i]]

if a = nums[3] = 5  then b = nums[nums[3]] = nums[5] = 4

We use a eqn so that we are able to retrieve both numbers
a + nb = 5 + 6 * 4 = 29

a => 29 % 6 = 5
b => 29 // 6 = 4
"""
