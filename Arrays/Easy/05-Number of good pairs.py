# https://leetcode.com/problems/number-of-good-pairs/

# Solution 1
# Time O(N) | Space O(N)
def GoodPairs(nums):
    dic = {}
    for val in nums:
        if val not in dic:
            dic[val] = 0   
        dic[val] += 1
        
    count = 0
    for num in dic:
        if dic[num] == 1:
            continue
        count += (dic[num] - 1) * (dic[num]) // 2 # Eqn for sum of n number n = n * (n + 1) // 2

    return count

"""
The first logic which came to my head on thinking is Solution 1.

The Solution 2 is just optimized version of Solution 1.
"""

# Solution 2
# TIme O(N) | Space O(N)
def GoodPairs(nums):
    dic, count = {}, 0
    for val in nums:
        if val in dic:
            count += dic[val]
            dic[val] += 1
        else:
            dic[val] = 1
            
    return count