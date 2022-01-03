# https://leetcode.com/problems/happy-number

# Solution 1 
# Time O(logN) | Space O(N) # Since finding the new value is of time logN as number of digits is given by logn
def happyNumber(n):
    s = set()
    while n!=1 and n not in s:
        s.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n==1

# Solution 2 - Linked List Cycle
# Time O(logN) | Space O(1)
def happyNumber(n):
    slow, fast = n, findnext(n)
    while slow != fast:
        slow = findnext(slow)
        fast = findnext(findnext(fast))
        
    return slow == 1
    
def findnext(n):
    return sum(int(i) ** 2 for i in str(n))