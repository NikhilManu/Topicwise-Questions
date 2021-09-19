# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

# Assume you cannot use length function.

# Time O(LogN) | Space O(1)
def findPosition(arr, target):
    start, end = 0, 1 # Starting with box of size 2
    while target > arr[end]:
        # Increasing size of box exponentially
        newStart = end + 1 # Cant update start before updating the end
        end = end + (end - start + 1) * 2 
        start = newStart
    
    return BinarySearch(arr, target, start, end)

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