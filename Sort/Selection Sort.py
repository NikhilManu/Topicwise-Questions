# Time O(N^2)
# Not stable Sorting
def SelectionSort(arr):
    for i in range(len(arr)):
        last = len(arr) - i - 1
        maxIdx = getMaxIdx(arr, 0, last)

        arr[last], arr[maxIdx] = arr[maxIdx], arr[last]

    return arr

def getMaxIdx(arr, start, end):
    max = start
    
    for i in range(start, end + 1):
        if arr[max] < arr[i]:
            max = i

    return max