# https://leetcode.com/problems/valid-perfect-square/

def isPerfectSquare(num):
    start, end = 0, num
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if mid * mid == num:
            return True
        elif mid * mid < num:
            start = mid + 1
        else:
            end = mid - 1
            
    return False