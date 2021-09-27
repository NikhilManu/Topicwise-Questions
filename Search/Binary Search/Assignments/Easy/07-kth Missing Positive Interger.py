# https://leetcode.com/problems/kth-missing-positive-number/

def FindInteger(nums, k):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] - mid - 1 < k:
            start = mid + 1
        else:
            end = mid - 1

    return start + k