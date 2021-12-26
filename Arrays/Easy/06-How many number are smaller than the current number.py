# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

# Time O(N) | Space O(N)
def smallerThanCurrent(nums):
    dic = {}
    for idx, num in enumerate(sorted(nums)):
        if num not in dic:
            dic[num] = idx # This allows to eliminate the problem of duplicate numbers
    
    res = []
    for num in nums:
        res.append(dic[num])
    
    return res