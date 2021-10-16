# 

# Sorting Algorithm is Easy, just sort and return the element at n/2 position

# Boyer-Moore Voting Algorithm
# Time O(N) | Space O(1)

def findMajority(nums):
    count = 0 
    curMajority = -1
    for num in nums:
        if count == 0:
            curMajority = num
            count += 1
        elif num != curMajority:
            count -= 1
        else:
            count += 1
    
    return curMajority

"""
Here given in the Question that majority element appears more than n/2 times.
So the sum of count of all other elements is always less than the majority element.

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]
The above example show where count become zero
So in the first portion the majority waws 7 and but was cancelled by 5 and 1
In the second portion no majority was found, 
in the third portion also no majority was found, but in the last portion 5 was the majority
"""