# Check array is sorted or Not

def isSorted(arr, idx):
    if idx == len(arr) - 1:
        return True
    
    return arr[idx] < arr[idx + 1] and isSorted(arr, idx + 1)

