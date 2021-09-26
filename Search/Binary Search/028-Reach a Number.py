# https://leetcode.com/problems/reach-a-number/

# 
# Didnt understand the logic of using binary search...Need to revisit
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