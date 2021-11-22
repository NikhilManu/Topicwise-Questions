# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# 
def CountSteps(num):
    return helper(num, 0)

def helper(num, steps):
    if num == 0:
        return steps
    
    if num % 2 == 0:
        return helper(num // 2, steps + 1)
    return helper(num - 1, steps + 1)