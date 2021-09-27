# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# Time O(LogN) | Space O(1)
def nextGreatestLetter(arr, target):
    start, end = 0, len(arr) - 1
    
    # if target >= arr[end]:
    #     return arr[0]
    
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return arr[start % len(arr)] 
    # at the last step start = end + 1, so if needed to wrap around, then remainder is 0 