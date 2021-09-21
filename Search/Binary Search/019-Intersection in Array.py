# https://leetcode.com/problems/intersection-of-two-arrays/

# This is not the Best Solution
def InterSection(nums1, nums2):
    big, small = nums1, nums2
    if len(nums1) < len(nums2):
        big, small = nums2, nums1
        
    res = []    
    big = set(big)
    small.sort()
    
    for value in big:
        if BinarySearch(small, value):
            res.append(value)
    
    return res

def BinarySearch(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False