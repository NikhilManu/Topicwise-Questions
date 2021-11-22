# Given a array, return the subset of the array, the array may contain duplicates

# Whenever a duplicate is encountered, add it only to newly created list of the previous step
# therefore the duplicate have to be side by side

def subsetDuplicate(arr):
    arr.sort() # we need the duplicates to be side by side
    res = [[]]
    start, end = 0, 0
    for i in range(len(arr)):
        start = 0
        if i > 0 and arr[i - 1] == arr[i]:
            start = end + 1
        end = len(res) - 1

        size = len(res)
        for j in range(start, size):
            res.append(res[j] + [arr[i]])

    return res

print(subsetDuplicate([1,2,2]))