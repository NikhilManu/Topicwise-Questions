# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

# Time O(log(maxSum)) | Space O(1)
def maxValue(n, i, maxSum):
    """
     0  ...    i  ...    n
    [1, .... , x, .... , 1]
    
    So Here we have to find value at index i which should be maximized,
    such that total sum of array should be less than or Equal to maxSum
    
    Also said that array should only contain positive numbers...ie... not even zeros
    
    So Here we will maxmize x and add sum of leftSide and sum of rightSide
    x + leftSIde + RightSide
    
    Array will be like a mountain,
                    i
    [1, .... , x-1, x, x-1, .... , 1]
    
    no of Elements on leftSide --> i
    no of Elements on RightSide --> n - i - 1
    """
    start, end = 1, maxSum # maxValue possible at index is in range [1, maxSum]
    res = 0
    while (start <=  end):
        mid = start + (end - start) // 2
        
        eleOnLeft = min(i, mid - 1) # There can be either i elements or only mid - 1 element
        leftSum = SequenceSum(eleOnLeft, mid - 1)
        leftSum += max(0, i - mid + 1) # Adding the remaining 1's to the leftSum
        
        eleOnRight = min(n - i - 1, mid - 1)
        rightSum = SequenceSum(eleOnRight, mid - 1)
        rightSum += max(0, n - i - 1 - mid + 1) # Adding the remaining 1's to the RightSum
        
        if mid + leftSum + rightSum <= maxSum:
            res = max(res, mid)
            start = mid + 1
        else:
            end = mid - 1
            
    return res

def SequenceSum(ele, x):
    """
    sum of range [1, n] --> n * (n + 1) // 2
    
    sum of range [x, n] --> (n * (n + 1) // 2) - (x * (x + 1) // 2)
    
    """
    totalSum = x * (x + 1) // 2
    rem = x - ele
    partialSum = rem * (rem + 1) // 2
    
    return totalSum - partialSum