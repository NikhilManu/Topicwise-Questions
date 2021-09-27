# https://leetcode.com/problems/split-array-largest-sum/

def SplitArray(nums, m):
    start, end = 0, 0

    for num in nums:
        start = max(start, num) # start will have minimum of the largest potential sum
        end += num # end will have the maximum of the largest potential sum

    while start < end:
        mid = start + (end - start) // 2  # mid can acts as potential minimized largest sum

        pieces, curSum = 1, 0
        for num in nums:
            if curSum + num > mid:
                curSum = num
                pieces += 1
            else:
                curSum += num

        if pieces > m:
            start = mid + 1
        else:
            end = mid

    return start # start == end 