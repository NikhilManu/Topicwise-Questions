# https://leetcode.com/problems/third-maximum-number/

# Whenever nth max or nth min is asked, it usually tells us to use a heap
# Since here it is said that 3rd Max, we can directly use 3 variables

# Time O(N) | Space O(1)
def ThirdMax(nums):
    m1, m2, m3 = float('-inf'), float('-inf'), float('-inf')
    
    for num in nums:
        if num > m1:
            m1, m2, m3 = num, m1, m2
        elif num > m2 and num != m1:
            m2, m3 = num, m2
        elif num > m3 and num != m2 and num != m1:
            m3 = num
            
    return m1 if m3 == float('-inf') else m3
