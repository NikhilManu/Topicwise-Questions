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
    
    # Now only Two Rows are remaining for searching the Target  
    # So now we can split each row into two halfs and perform normal BinarySearch
        
    if matrix[rstart][cmid] >= target: # Search in left Side of first Row
        return BinarySearch(matrix, rstart, 0, cmid, target)
    
    elif matrix[rstart][cmid] < target <= matrix[rstart][cols - 1]: # Search in Right Side of first Row
        return BinarySearch(matrix, rstart, cmid + 1, cols - 1, target)
    
    if matrix[rstart + 1][cmid] >= target: # Search in left Side of Second Row
        return BinarySearch(matrix, rstart + 1, 0, cmid, target)    
    
    elif matrix[rstart + 1][cmid] < target: # Search in Right Side of Second Row
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