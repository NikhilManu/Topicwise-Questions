# https://leetcode.com/problems/reach-a-number/

# Time O(K) | Space O(1)
def ReachNumber(target):
    """
    Let say our target -> 13
    
    1 + 2 + 3 + 4 + 5 --> 15
    
    so our delta = (15 - 13) = 2,
    we need to divide delta by 2 and
    we need to just subtract  from here
    => -1 + 2 + 3 + 4 + 5
    
    if our move is odd and also delta is odd, then next move added is even
    so even + odd = odd
    so we have to add it again 
    
    so if out move is odd, k + 2
    if out move is even, k + 1
    """
    
    target = abs(target)
    k = 0
    while target > 0:
        k += 1
        target -= k
        
    if target % 2 == 0:
        return k
    else:
        if k % 2 == 0:
            return k + 1
        else:
            return k + 2

# Approach II - Binary Search the number or steps
# Time O(log(Target)) | Space O(1)
def reachNumber(target):
    steps = Bsearch(abs(target))
    diff = steps * (steps + 1) // 2 - abs(target)
    
    """
        Adjust steps:
        - Determine the difference (diff) between the total
          distance traveled, min_steps * (min_steps + 1) // 2,
          and target.
        - If diff is 0, min_steps does not change.
        - If diff is even, it is possible to flip a step from
          positive to negative to get target. Again, min_steps
          does not change.
        - If diff is odd, we need to add one or two steps to
          create an even difference, at which point we can flip
          one or more steps to get target.
    """
    if diff % 2:
        return steps + 1 + steps % 2 # same as above case, Just wrote it in one line
    return steps

def Bsearch(target):
    start, end = 0, abs(target)
    while start < end:
        minSteps = start + (end - start) // 2
        
        canReach = minSteps * (minSteps + 1) // 2 >= target
        if canReach:
            end = minSteps
        else:
            start = minSteps + 1
            
    return end