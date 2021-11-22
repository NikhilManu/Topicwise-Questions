# Given a string, return all the subset of that string 

# subsequence is same as subset. For a string we use the term subsequence
# order should remain the same
# For subset problem, at every point we have two choices, take and element or ignore it.

# Method 1 
def StrSubseqI(string):
    return helperI("", string, [])

def helperI(cur, string, res):
    if not string:
        res.append(cur)
        return 

    ch = string[0]
    helperI(cur + ch, string[1:], res)
    helperI(cur, string[1:], res)

    return res

# Method 2
def StrSubseqII(string):
    return helperII("", string)

def helperII(cur, string):
    if not string:
        return [cur]

    ch = string[0]
    left = helperII(cur + ch, string[1:])
    right = helperII(cur, string[1:])

    left.extend(right) # or return left + right
    return left
