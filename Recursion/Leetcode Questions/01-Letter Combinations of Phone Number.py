# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Time O(4^n * n) | Space O(4^n * n)
# Method 1
DigitToString = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
    }
def letterCombinations(digits):
    return helper(digits, "", [])

def helper(digits, comb, res):
    if not digits:
        res.append(comb)
        return
    
    string = DigitToString[digits[0]]
    for char in string:
        helper(digits[1:], comb + char, res)

    return res

# Method 2 - By not passing the resultant array in the argument
def PhoneCombinations(digits):
    return helper(digits, "") if digits else []

def helper(digits, comb):
    if not digits:
        return [comb]
    
    res = []
    string = DigitToString[digits[0]]
    for char in string:
        res.extend(helper(digits[1:], comb + char))

    return res