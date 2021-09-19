# https://leetcode.com/problems/sqrtx/ 

def Sqrt(x):
    if x == 0 or x == 1:
        return x

    start, end = 2, x

    while start <= end:
        mid = start + (end - start) // 2
        
        if mid * mid == x:
            return mid
        
        if mid * mid > x:
            end = mid - 1
        else:
            start = mid + 1

    # When there is no perfect square, end is the the value on the left
    # of where it would have been (rounding down). If we were rounding up, 
    # we would return start

    return end  