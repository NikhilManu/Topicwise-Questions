# https://leetcode.com/problems/merge-sorted-array/

# Since Insertion Sort Works good on Partially sorted data
# key point to note is the date should be filled from the back 

# Time O(n + m)
def Merge(nums1, m, nums2, n):
    j = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[j]
        j += 1
        
    return Insertion(nums1)

def Insertion(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


# Solution 2
def Merge(nums1, m, nums2, n):
    i, j = m-1, n-1
    k = len(nums1) - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            
        k -= 1
        
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

    return nums1
            