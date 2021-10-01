# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

# Time O(n logn) | Space O(n)
def maxFrequency(nums, k):
    nums.sort()
    pre, best = [0], 1

    # Create a prefixSum array so we can know sum till the a index i
    for num in nums:
        pre.append(pre[-1] + num)

    for i in range(len(nums)):
        start, end = 0, i
        bestIdx = i

        while start <= end:
            mid = start + (end - start) // 2

            prefixSum = pre[i] - pre[mid]  # sum of range(mid, i - 1)

            if prefixSum + k >= (i - mid) * nums[i]: # (i - mid) gives the length of the window, and we make every number in the window to nums[i]
                bestIdx = mid
                end = mid - 1 # making the window bigger
            else:
                start = mid + 1 # making the window smaller

        best = max(best, i - bestIdx + 1)

    return best


# Best Approach is sliding window, which takes O(N) Time