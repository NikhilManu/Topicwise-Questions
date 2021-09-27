# https://leetcode.com/problems/find-in-mountain-array/
# Combination of Peak Element and Order Agnostic Binary Search

# Time O(logN) | Space O(1)
def findInMountainArray(self, target: int, arr: 'MountainArray'): # MountainArray is an class
    peakIdx = self.BinarySearchPeak(arr)
    AscendingSide = self.OrderAgnosticBS(arr, target, 0, peakIdx)
    if AscendingSide != -1:
        return AscendingSide
    return self.OrderAgnosticBS(arr, target, peakIdx + 1, arr.length() - 1)

def BinarySearchPeak(self, arr):
    start, end = 0, arr.length() - 1
    while start < end:
        mid = start + (end - start) // 2

        if arr.get(mid) > arr.get(mid + 1): 
            end = mid 
        else: 
            start = mid + 1

    return start 

def OrderAgnosticBS(self, arr, target, start, end):
    # find array is Sorted Ascending or Descending
    isAscending = arr.get(start) < arr.get(end)

    while start <= end:
        mid = start + (end - start) // 2

        if arr.get(mid) == target:
            return mid

        if isAscending:
            if arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr.get(mid) < target:
                end = mid - 1
            else:
                start = mid + 1

    return -1