# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Time O(n * log(m)) --> m is length of smaller array | Space O(1)
def intersect(nums1, nums2):
    if len(nums1) < len(nums2):
        return intersect(nums2, nums1)
    
    nums1.sort(); 
    res = []
    for num in nums2:
        idx = BinarySearch(nums1, num, 0, len(nums1) - 1)
        if idx == -1:
            continue
        res.append(num)
        nums1.remove(num) # This method is costly, we can use a set to keep track of visited index
        
    return res

def BinarySearch(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


# Using two pointer would be better than using Binary Search, since it can be done without any space and also will not require costly function such as nameofArray.remove()