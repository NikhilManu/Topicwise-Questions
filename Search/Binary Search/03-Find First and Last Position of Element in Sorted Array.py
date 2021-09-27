# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def SearchRange(nums, target):
    left = BinarySearch(nums, target, True)
    if left == -1:
        return [-1, -1]
    right = BinarySearch(nums, target, False)
    return [left, right]

def BinarySearch(arr, target, findLeftmost):
    start, end = 0, len(arr) - 1
    index = -1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            index = mid
            if findLeftmost:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return index