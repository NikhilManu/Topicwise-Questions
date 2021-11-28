# https://leetcode.com/problems/power-of-four 

# Time O() | Space O()
def isPowerOfFour(n, cur = 1):
    if cur > n:
        return False
    
    if cur == n:
        return True
    
    return isPowerOfFour(n, cur * 4)