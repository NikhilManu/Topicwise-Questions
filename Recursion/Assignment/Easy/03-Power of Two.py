# https://leetcode.com/problems/power-of-two/

# Time O() | Space O()
def isPowerOfTwo(n, cur = 1):
    if cur > n:
        return False
    
    if cur == n:
        return True
    
    return isPowerOfTwo(n, cur * 2)