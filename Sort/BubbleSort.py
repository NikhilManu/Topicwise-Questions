# Time O(N^2)
def Bubble(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr

"""
Stable Sorting:

Consider a array 
[10, (20), 20, 30, (10)] --> Sorting --> [10, (10), (20), 20, 30]
Here before and after sorting 10 was before (10). The order was maintained. So this is called Stable Sorting

if the array was sorted [(10), 10, 20, (20), 30], this would have been a unstable sorting Algorithm

"""
