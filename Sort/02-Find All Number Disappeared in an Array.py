# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Time O(N) | Space O(1) --> if res is not included
def findAllNumbers(array):
    res = []
    CyclicSort(array)
    for idx in range(len(array)):
        if idx != array[idx] - 1:
            res.append(idx + 1)
    return res
    
def CyclicSort(array):
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx] - 1
        if array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1