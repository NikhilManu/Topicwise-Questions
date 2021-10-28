# Given Array of integers, return the subset of the array

# Time and Space O(N * 2^N)
def Subset(arr):
    res = [[]]
    for num in arr:
        size = len(size)
        for i in range(size):
            cur = res[i][:]
            res.append(cur + [num])
    return res