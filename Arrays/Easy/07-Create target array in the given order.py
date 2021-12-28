# https://leetcode.com/problems/create-target-array-in-the-given-order/

# Time O(N ^ 2) | Space O(N)
def createTargetArray(nums, index):
    target = [-1] * len(nums)
    for num, idx in zip(nums, index):
        if target[idx] != -1:   
            for i in reversed(range(idx, len(target))):
                target[i] = target[i - 1]    
        
        target[idx] = num
    return target
