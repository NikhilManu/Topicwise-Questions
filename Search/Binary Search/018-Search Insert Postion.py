# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums, target):
    return BinarySearch(nums, target)

def BinarySearch(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start