# https://leetcode.com/problems/fair-candy-swap/

# Time O(n*log(m)) | Space O(1)
def FairCandySwap(aliceSizes, bobSizes):
    asum, bsum = sum(aliceSizes), sum(bobSizes)
    
    b = sorted(bobSizes)
    for x in aliceSizes:
        val = x + (bsum - asum)// 2
        if BinarySearch(b, val):
            return [x, val]

def BinarySearch(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


# Instead of doing Binary Search in the array, we can use hashmap and find the search for it