# https://leetcode.com/problems/power-of-three

# Time O() | Space O()
def isPowerOfThree(n, cur = 1):
    if cur > n:
        return False
    
    if cur == n:
        return True
    
    return isPowerOfThree(n, cur * 3)