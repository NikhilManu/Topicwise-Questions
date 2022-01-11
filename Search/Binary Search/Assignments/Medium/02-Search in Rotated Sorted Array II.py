# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# Approach 1 - Using Pivot
# Time O(logN) | Space O(1)
def search(nums, target):
    pivotIdx = findPivot(nums)
    if pivotIdx == -1:
        return BinarySearch(nums, target, 0, len(nums) - 1)
    
    start = 0 if target >= nums[0] else pivotIdx + 1
    end = pivotIdx if start == 0 else len(nums) - 1
    return BinarySearch(nums, target, start, end)

def findPivot(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]: 
            return mid
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        
        if arr[mid] == arr[start] == arr[end]: # [2, 9, 2, 2, 2] is an example case
            # we have to check if element at the start or end are pivot.
            if start < len(arr) - 1 and arr[start] > arr[start + 1]:
                return start
            start += 1
            if arr[end] < arr[end - 1]:
                return end - 1 
            end -= 1
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]): # arr[mid] > arr[end] ensures that we look into the correct half
            start = mid + 1
        else:
            end = mid - 1
            
    return -1

def BinarySearch(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False

# Approach 2 - using the fact one side of the array remains sorted always
# Time O(log N) | Space O(1)
def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            return True
        
        while start < mid and nums[start] == nums[mid]:
            start += 1
        
        if nums[start] <= nums[mid]: 
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return False