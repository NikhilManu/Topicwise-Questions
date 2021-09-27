# https://leetcode.com/problems/find-right-interval/

# Time O(n logn) | Space O(n)
def findRightInterval(intervals):
    # we need to remember the orginal indices of intervals
    idx = {tuple(inv):i for i, inv in enumerate(intervals)} 
    intervals.sort()
    res = [-1] * len(intervals)
    
    for i in range(len(intervals) - 1):
        target = intervals[i][1]
        pos = BinarySearch(intervals, target, i, len(intervals) - 1)
        
        if pos == len(intervals):
            continue
        
        # res[i] --> should be the corresponding index of the interval
        # res[i] = smallest index of the interval where startJ >= endI
        res[idx[tuple(intervals[i])]] = idx[tuple(intervals[pos])] 
        
    return res
        

def BinarySearch(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid][0] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start