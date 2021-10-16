# https://leetcode.com/problems/missing-number/

# Time O(n) | Space O(1)
def MissingNumber(array):
    CyclicSort(array)
    for idx in range(len(array)):
        if idx != array[idx]:
            return idx
    return len(array)
    
def CyclicSort(array):
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx]
        if array[idx] < len(array) and array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1


# Another Solution efficent than above Solution
def MissingNumber(array):
    n = len(array)
    expectedSum = n * (n + 1) // 2
        
    for num in array:
        expectedSum -= num
        
    return expectedSum 