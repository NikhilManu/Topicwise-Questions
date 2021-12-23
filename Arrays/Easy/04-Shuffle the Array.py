# https://leetcode.com/problems/shuffle-the-array/

# Solution 1
# Time O(N) | Space O(N)
def shuffle(nums, n):
    a, b = 0, n
    ans = []
    while a < n:
        ans.append(nums[a])
        ans.append(nums[b])
        a += 1; b += 1

    return ans

# Time O(N) | Space O(1)
def shuffle(nums, n):
    for i in range(len(nums)):
        j = i
        while nums[i] > 0:
            j = getIdx(j, n)
            nums[i], nums[j] = nums[j], -nums[i]
            
    for i in range(len(nums)):
        nums[i] *= -1
        
    return nums

def getIdx(self, idx, n):
    return idx * 2 if idx < n else (idx - n) * 2 + 1

"""
Each number have a fixed index, so we need to create a formula for getting the orginal index of each number

After that we just need to swap each number to there orginal index, once they reach their orginal index mark them -ve so that
they are not processed again

Finally remove the negative marking and return the array
"""