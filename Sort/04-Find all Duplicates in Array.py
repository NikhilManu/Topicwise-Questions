# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Time O(N)
def findAllDupsinArray(array):
    res = []
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx] - 1
        if array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1
    
    for i in range(len(array)):
        if array[i] != i + 1:
            res.append(array[i])
    return res