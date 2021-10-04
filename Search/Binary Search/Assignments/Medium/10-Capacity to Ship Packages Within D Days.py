# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# Time O(N log(Sum(arr))) | Space O(1)
def shipWithinDdays(weights, days):
    # Start should not be assigned as zero    
    start, end = max(weights), sum(weights) 
    while start <= end:
        mid = start + (end - start) // 2

        if canShip(weights, days, mid):
            end = mid - 1
        else:
            start = mid + 1

    return start

def canShip(weights, days, capacity):
    curCap, curDays = 0, 1
    for weight in weights:
        curCap += weight
        if curCap > capacity:
            curCap = weight
            curDays += 1
            if curDays > days:
                return False
    
    return True