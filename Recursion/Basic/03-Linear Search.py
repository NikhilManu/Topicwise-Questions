# Linear Search Using Recursion
def Lsearch1(arr, target, idx):
    if idx == len(arr):
        return -1
    if arr[idx] == target:
        return idx

    return Lsearch(arr, target, idx + 1)

# Find All Indices
def Lsearch(arr, target, idx, res):
    if idx == len(arr):
        return res
    if arr[idx] == target:
        res.append(idx)

    return Lsearch(arr, target, idx + 1, res)

# Actually this is a bad Approach
def Lsearch(arr, target, idx):
    res = []
    if idx == len(arr):
        return res 

    if arr[idx] == target:
        res.append(idx)

    ansFromBelowCalls = Lsearch(arr, target, idx + 1)
    res += ansFromBelowCalls
    return res

