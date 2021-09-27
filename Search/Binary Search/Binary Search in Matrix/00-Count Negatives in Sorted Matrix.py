# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Time O(N + M) | Space O(1)
def CountNegatives(matrix):
    return RowColMatrixBS(matrix)

def RowColMatrixBS(matrix, target = -1):
    r, c = 0, len(matrix[0]) - 1
    count = 0
    while r < len(matrix) and c >= 0:
        if matrix[r][c] <= target:
            count += (len(matrix) - r)
            c -= 1
        else:
            r += 1

    return count 

