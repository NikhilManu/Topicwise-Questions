# Ceiling --> smallest element in array greater than or equal to target value
# floor --> greatest element in array smaller than or equal to target value

# Time O(logN)
def findCeiling(arr, target):
    return BinarySearchCeiling(arr, target)

def BinarySearchCeiling(arr, target):
    start, end = 0, len(arr) - 1

    if target > arr[end]:
        return "Doesnt Exist"
    # find array is Sorted Ascending or Descending
    isAscending = arr[start] < arr[end]
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        
        if isAscending:
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target:
                end = mid - 1
            else:
                start = mid + 1

    return start # we return start since at the end loop start = end + 1


# if floor is asked --> return end if number is not found