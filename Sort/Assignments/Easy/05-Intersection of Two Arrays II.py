# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Time O(nlogn + mlogm) | Space O(min(n,m))
def IntersectionOfArray(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return res