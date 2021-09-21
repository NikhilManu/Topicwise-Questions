"""
[
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [28, 29, 37, 49],
    [33, 34, 38, 50]
]
"""
# Row and col of the matrix is sorted

# Time O(N) | Space O(1)
def MatrixBS(matrix, target):
    r, c = 0, len(matrix) - 1

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return [r,c]
        elif matrix[r][c] < target:
            r += 1
        else:
            c -= 1

    return [-1, -1]
