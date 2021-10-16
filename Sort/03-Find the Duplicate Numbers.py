# https://leetcode.com/problems/find-the-duplicate-number/

# Time O(N)  
def findTheDup(array):
    idx = 0 
    while idx < len(array):
        if array[idx] != idx + 1:
            correctIdx = array[idx] - 1
            if array[idx] != array[correctIdx]:
                array[idx], array[correctIdx] = array[correctIdx], array[idx]
            else:
                return array[idx]
        else:
            idx += 1
        
    return -1

# Here in the first Solution we are modifying the array, but the follow up tells to not modify the array
# Do the linkedLIst Cycle logic
def findTheDup(array):
    slow, fast = 0, 0
    
    while True:
        slow = array[slow]
        fast = array[array[fast]]
        if slow == fast:
            break
            
    slow = 0
    while fast != slow:
        fast = array[fast]
        slow = array[slow]
        
    return fast