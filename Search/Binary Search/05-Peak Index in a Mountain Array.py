# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# TIme o(logN) | Space O(1)
def findPeak(arr):
    return BinarySearch(arr)

def BinarySearch(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[mid + 1]: # descending part of array
            end = mid # end != mid - 1, since mid can be potential answer
        else:
            # Ascending part of array
            start = mid + 1 # since ele[mid + 1] > ele[mid]
    
    # start and end are always trying to find max element till that time, so when start == end means we found the peak
    return start # or end


    # find Peak Element --> https://leetcode.com/problems/find-peak-element/submissions/
    # Literally same answer, just copy paste the code