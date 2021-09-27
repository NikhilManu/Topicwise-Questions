# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Time O(logN) | Space O(1)
def findMin(nums):
    pivot = findPivot(nums)
    if pivot == -1:
        return nums[0]
    
    return nums[pivot]
    
# Same as finding the pivot Index, just add +1
def findPivot(nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start)//2
        
        if mid < end and nums[mid] > nums[mid + 1]:
            return mid + 1
        elif mid > start and nums[mid - 1] > nums[mid]:
            return mid 
        
        if nums[start] > nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return -1