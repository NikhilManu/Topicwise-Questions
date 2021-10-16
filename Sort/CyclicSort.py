def CyclicSort(array):
    idx = 0 
    while idx < len(array):
        correctIdx = array[idx] - 1
        if array[idx] != array[correctIdx]:
            array[idx], array[correctIdx] = array[correctIdx], array[idx]
        else:
            idx += 1
    return array

# Cyclic Sort is done when array of range [1, n] is given
# Here on the worse Case 2n - 1 Comaparsions are made 
# ie.. N swaps and the N - 1 comparisons