# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

# Time O(N) | Space O(N)
def kidsWithCandies(candies, extraCandies):
    maxCandies = max(candies)
    res = []
    for i in candies:
        res.append(i + extraCandies >= maxCandies)
        
    return res