# https://leetcode.com/problems/first-missing-positive/

# Time O(N) | Space O(1)
def findFirstPositive(array):
    CyclicSort(array)
    for idx in range(len(array)):
        if idx != array[idx] - 1:
            return idx + 1
    return len(array) + 1

def CyclicSort(array):
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx] - 1
        if array[idx] > 0 and array[idx] < len(array) and array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1