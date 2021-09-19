# https://leetcode.com/problems/first-bad-version/

def BadVersion(n):
    start, end = 1, n
    badVersion = -1
    while start <= end:
        mid = start + (end - start) // 2

        bad = isBadVersion(mid) # returns True or False
        if bad:
            badVersion = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return badVersion