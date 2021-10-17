# https://leetcode.com/problems/intersection-of-two-arrays/

# Time O(nlogn + mlogm) | Space O(min(n,m))
def IntersectionOfArray(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not res or res[-1] != nums1[i]: # add to res only if it is empty or the last element is not equal to current
                res.append(nums1[i])
            i += 1
            j += 1
            while i > 0 and i < len(nums1) and nums1[i] == nums1[i - 1]: #
                i += 1                                                   #  Skipping the Duplicates
            while j > 0 and j < len(nums2) and nums2[j] == nums2[j - 1]: #
                j += 1                                                   #
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
            
    return res