# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

# Time O(m * n + L) | Space O(m * n)
def OddCells(m, n, indices):
    res = [[0]*n for _ in range(m)]
    for row, col in indices:
        for c in range(n):
            res[row][c] += 1
        for r in range(m):
            res[r][col] += 1
            
    count = 0
    for row in res:
        for val in row:
            count += 1 if val % 2 else 0
            
    return count