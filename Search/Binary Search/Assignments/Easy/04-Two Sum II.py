# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def TwoSum(array, target):
    for i in range(len(array)):
        second = target - array[i]
        secondIdx = BinarySearch(array, second, i + 1, len(array) - 1)
        if secondIdx != -1:
            return [i + 1, secondIdx + 1]

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