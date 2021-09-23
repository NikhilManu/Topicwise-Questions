# 

# 
def specialArray(nums):
    nums.sort()
    for i in range(len(nums) + 1): # len(nums) is the highest possible output, 
        res = BinarySearch(nums, i)
        if res == i:
            return res
        
    return -1
        
def BinarySearch(arr, target):
    start, end = 0, len(arr) - 1
    idx = -1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            idx = mid
            end = mid - 1 # To find the leftmost index of the target
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    # if idx == -1 then start is the position with smallest number which is greater than the target
    # if idx != -1 then we find the left most index of the target
    return len(arr) - idx if idx != -1 else len(arr) - start