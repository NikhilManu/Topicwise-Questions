# Given an string, return the permutation of the string

def Permutation(string):
    return helper([],string, [])

def helper(cur, string, res):
    if not string:
        res.append(cur)
        return 

    ch = string[0]
    for i in range(len(cur) + 1):
        first = cur[:i]
        second = cur[i:]
        helper(first + ch + second,string[1:], res)

    return res

# Method 2
def getPermutation(string):
    return permHelper([], string)

def permHelper(cur,string):
    if not string:
        return [cur]
    
    res, ch = [], string[0]
    for i in range(len(cur) + 1):
        first = cur[:i]
        second = cur[i:]
        res.extend(permHelper(first + ch + second, string[1:]))

    return res
    