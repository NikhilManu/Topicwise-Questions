# https://leetcode.com/problems/check-if-n-and-its-double-exist/

# Time O(n * logn) | Space O(1)
def check(arr):
    arr.sort()
    for i in range(len(arr)):
        x = arr[i]
        res = BinarySearch(arr, x * 2)
        if res != -1 and res != i:
            return True
    return False

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

    return -1