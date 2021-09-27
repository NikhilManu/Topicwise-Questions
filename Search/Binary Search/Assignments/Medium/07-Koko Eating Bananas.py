# https://leetcode.com/problems/koko-eating-bananas/

# Time O(n log(max(piles))) | Space O(1)
def findSpeed(piles, h):
    start, end = 1, max(piles)
    total = end
    while start < end:
        mid = start + (end - start) // 2
        
        if isPossible(piles, mid) <= h:
            end = mid
            
        else:
            start = mid + 1
            
    return start
        
    
def isPossible(piles, k):
    time = 0
    for pile in piles:
        time += pile // k
        # if she cant complete a pile at the rate of k Bananas, just add 1 hour 
        if pile % k != 0:
            time += 1
        
    return time 