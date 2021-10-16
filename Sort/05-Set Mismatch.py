# https://leetcode.com/problems/set-mismatch/

# Time O(N) | Space O(1)
def findErrorNums(array):
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx] - 1
        if array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1

    for i in range(len(array)):
        if array[i] != i + 1:
            return [array[i],i + 1]
    return []
