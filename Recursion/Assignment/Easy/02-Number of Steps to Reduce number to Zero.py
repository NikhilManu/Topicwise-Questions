# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# 
def numOfSteps(num, steps=0):
    if num == 0:
        return steps
    
    if num % 2 == 0:
        return numOfSteps(num//2, steps + 1)
    
    return numOfSteps(num - 1, steps + 1)