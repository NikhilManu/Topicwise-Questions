# https://leetcode.com/problems/guess-number-higher-or-lower/

def guessNumber(x):
    start, end = 0, n
    while start <= end:
        mid = start + (end - start) // 2
        
        pick = guess(mid) # guess return -1, 0 or 1
        if pick == 0:
            return mid
        elif pick == -1:
            end = mid - 1
        else:
            start = mid + 1
            