# https://leetcode.com/problems/single-element-in-a-sorted-array/

# Time log(n) | Space O(1)
def findElement(nums):
    return BinarySearchModified(nums)

def BinarySearchModified(arr):
    start, end = 0, len(arr) - 1 
    while start < end:
        mid = start + (end - start) // 2
        
        # In the array if each element appears twice, first one will be in even pos, and next will be in odd pos
        # If the above condition is violated then it means, solution is to the left side of the array, else to right side
        cond1 = mid % 2 != 0 and arr[mid] == arr[mid - 1]
        cond2 = mid % 2 == 0 and arr[mid] == arr[mid + 1]
        if cond1 or cond2:
            start = mid + 1
        else:
            end = mid

    return arr[end] # Here end == start