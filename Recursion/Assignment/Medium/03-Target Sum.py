# https://leetcode.com/problems/target-sum/

# Time O(2 ^ n) | Space O(n)
# Solution Timeout
def targetSum(nums, target):
    return getWays(nums, target, 0)

def getWays(nums, target, idx):
    if idx == len(nums):
        if target == 0:
            return 1
        return 0
    
    return getWays(nums, target - nums[idx], idx + 1) + getWays(nums, target + nums[idx], idx + 1)

# Time O(s * n) | Space O(s * n) where s is sum of nums array 
def targetSum(nums, target):
    return getWays(nums, target, 0, {})

def getWays(nums, target, idx, mem):
    if (idx, target) not in mem:
        if idx == len(nums):
            if target == 0:
                return 1
            return 0
    
        mem[(idx, target)] = getWays(nums, target - nums[idx], idx + 1, mem) + getWays(nums, target + nums[idx], idx + 1, mem)
        
    return mem[(idx, target)]