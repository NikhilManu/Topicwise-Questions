# https://leetcode.com/problems/minimum-absolute-sum-difference/

# Time O(n logn) | Space O(1)
def minSumDIff(nums1, nums2):
    snums1 = sorted(nums1) # making list ready for Binary search
    total = 0
    for i in range(len(nums1)):
        total += abs(nums1[i] - nums2[i])
        
    best = total
    
    for x, y in zip(nums1, nums2):
        currDiff = abs(x - y)
        
        idx = BinarySearch(snums1, y)
        # if not element exist, idx gives you index of the next largest element
        # but idx - 1 might be also a potential answer, so we check that also
        if 0 <= idx < len(snums1):
            val = snums1[idx]
            
            potentialBest = total - currDiff + abs(val - y)
            best = min(best, potentialBest)
            
        if idx - 1 < len(snums1):
            val = snums1[idx - 1] 
            
            potentialBest = total - currDiff + abs(val - y)
            best = min(best, potentialBest)
        
    
    return best % (10 ** 9 + 7)
    

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
    
    return start