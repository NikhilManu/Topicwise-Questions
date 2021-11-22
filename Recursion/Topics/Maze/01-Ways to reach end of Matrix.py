# Number of ways to reach end of a matrix

def ways(row, col):
    if row == 1 or col == 1:
        return 1

    left = ways(row - 1, col)
    right = ways(row, col - 1)
    return left + right

# All path for reaching end of a matrix, but you can only move right or down
def allPath(cur, row, col):
    if row == 1 and col == 1:
        return [cur]

    path = []
    if row > 1:
        path.extend(allPath(cur + 'D', row - 1, col))
    
    if col > 1:
        path.extend(allPath(cur + 'R', row, col - 1))

    return path

# All path for reaching end of a matrix (can move diagonal also)
def allPathDiagonal(cur, row, col):
    if row == 1 and col == 1:
        return [cur]

    path = []
    if row > 1 and col > 1:
        path.extend(allPathDiagonal(cur + 'd', row - 1, col - 1))

    if row > 1:
        path.extend(allPathDiagonal(cur + 'D', row - 1, col))
    
    if col > 1:
        path.extend(allPathDiagonal(cur + 'R', row, col - 1))


    return path

print(allPathDiagonal("", 3, 3))