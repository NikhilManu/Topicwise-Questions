"""
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [10, 11, 12, 13]
]
"""
# Time O(logN + logM) | Space O(1)
def search(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0]) # matrix may be empty
    
    if rows == 1:
        return BinarySearch(matrix, 0, 0, cols - 1, target)

    rstart, rend = 0, rows - 1
    cmid = cols // 2

    # Run till 2 rows are only remaining
    while rstart < rend - 1: # while this is true, it will have more than 2 rows
        mid = rstart + (rend - rstart) // 2

        if matrix[mid][cmid] == target:
            return [mid ,cmid]
        elif matrix[mid][cmid] < target:
            rstart = mid
        else:
            rend = mid
    
    # Now we have only two rows
    # Check whether the target is in the col of the 2 rows
    if matrix[rstart][cmid] == target:
        return [rstart, cmid]
    if matrix[rstart + 1][cmid] == target:
        return [rstart + 1, cmid]

    # Search in 1st Half 
    if matrix[rstart][cmid - 1] >= target:
        return BinarySearch(matrix, rstart, 0, cmid - 1, target)

    # Search in 2nd Half
    if matrix[rstart][cmid + 1] >= target and matrix[rstart][cols - 1] >= target:
        return BinarySearch(matrix, rstart, cmid + 1, cols - 1, target)

    # Search in the 3rd Half
    if matrix[rstart + 1][cmid - 1] >= target:
        return BinarySearch(matrix, rstart + 1, 0, cmid - 1, target)

    # Search in the 4th Half
    if matrix[rstart] + 1[cmid + 1] >= target:
        return BinarySearch(matrix, rstart + 1, cmid + 1, cols - 1, target)

# Searching in the row provided
def BinarySearch(matrix, row, cstart, cend, target):
    while cstart <= cend:
        mid = cstart + (cend - cstart) // 2

        if matrix[row][mid] == target:
            return [row, mid]
        elif matrix[row][mid] < target:
            cstart = mid + 1
        else:
            cend = mid - 1

    return [-1, -1]