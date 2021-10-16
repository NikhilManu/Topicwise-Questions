# https://leetcode.com/problems/contains-duplicate/

# Time O(n logn) | Space O(1)
def ContainsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
        
    return False

# Time O(N) | Space O(1)
def ContainsDuplicate(nums):
    lookup = set()
    for num in nums:
        if num in lookup:
            return True
        lookup.add(num)

    return False