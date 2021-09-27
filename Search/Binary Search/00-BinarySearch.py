# Assuming the array is sorted Ascending Order
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

# Order Agnostic Binary Search
def OrderAgnosticBS(arr, target):
    start, end = 0, len(arr) - 1

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

    return -1
