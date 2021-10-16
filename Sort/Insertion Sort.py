# Worst Time - O(N^2)
# Best Time - O(N) 
# Stable Sorting Algorithm
# Good for partially sorted Algorithm

def Insertion(arr):
    for i in range(len(arr) - 1):
        for j in reversed(range(i + 1, 0)):
            if arr[j] < arr[j-1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr