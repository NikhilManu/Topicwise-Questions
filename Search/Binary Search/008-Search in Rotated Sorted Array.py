# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Approach 1 --> Find the Pivot, then search the 2 halves.
def search(nums, target):
    pivotIdx = findPivot(nums)
    if pivotIdx == -1: # if pivot not found then it means array is sorted
        return BinarySearch(nums, target, 0, len(nums) - 1)
    
    if target >= nums[0]:
        return BinarySearch(nums, target, 0, pivotIdx)
    return BinarySearch(nums, target, pivotIdx + 1, len(nums) - 1)

# This will not work for Duplicate Values    
def findPivot(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]: 
            return mid
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1
        
        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return -1

def findPivotWithDuplicates(arr):
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
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1