# https://leetcode.com/problems/arranging-coins/

def ArrangingCoin(n):
    start, end = 0, n
    while start <= end:
        mid = start + (end - start) // 2
        
        cur = mid * (mid + 1) // 2
        
        if cur > n:
            end = mid - 1
        elif cur < n:
            start = mid + 1
        else:
            return mid
    
    return end