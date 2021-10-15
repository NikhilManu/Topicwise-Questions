# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time O(log(m + n))
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    totalLength = len(nums1) + len(nums2)
    half = totalLength // 2 
    
    start, end = 0, len(nums1) - 1
    while True:
        midIdx1 = start + (end - start) // 2 
        midIdx2 = half - (midIdx1 + 1) - 1
        
        l1 = nums1[midIdx1] if midIdx1 >= 0 else float('-inf')
        l2 = nums2[midIdx2] if midIdx2 >= 0 else float('-inf')
        
        r1 = nums1[midIdx1 + 1] if midIdx1 + 1 < len(nums1) else float('inf')
        r2 = nums2[midIdx2 + 1] if midIdx2 + 1 < len(nums2) else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            if totalLength % 2:
                return min(r1, r2)
            
            return (max(l1, l2) + min(r1, r2)) / 2
        elif l1 > r2:
            end = midIdx1 - 1
        else:
            start = midIdx1 + 1

"""
arr1 -> [ 1, 3, 4, 7, 10, 12]
arr2 -> [ 2, 3, 6, 15 ]

So split the smaller array larger array in such a manner that 
leftPartition of arr1 and arr2 should be LeftPartition of sorted(arr1 + arr2)

so at any point after finding the partition of both array we need to check
left1 <= right2 and left2 <= right1 
ie...

case 1

1, 3, 4, 7 | 10, 12
        2  | 3, 6, 15

Here 7 is greater than 3 so the Partition is not correct

case 2
1, 3, 4 | 7, 10, 12
   2, 3 | 6, 15

Here the Partition is correct since all the values in the left Partition are less than or equal to 
values in the right partition
"""