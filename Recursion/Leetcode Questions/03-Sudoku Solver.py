# https://leetcode.com/problems/sudoku-solver/

# Similar to N-Queens and N-Knights (Backtracking)

# Time O(9 ^ (n^2)) | Space O(N^2) --> we can also say Time and Space is O(1) since it is 9 x 9 board
def sudokuSolver(board):
    solve(board, 0, 0)
    return board
    
def solve(board, row, col):
    emptyCell = getEmptyCell(board)
    if not emptyCell:
        return True
    
    row, col = emptyCell
    for num in range(1, 10):
        if isSafe(board, row, col, str(num)):
            board[row][col] = str(num)
            if solve(board, row, col):
                return True
            
            board[row][col] = "."
            
    return False

def isSafe(board, row, col, num):
    for i in range(len(board)):
        if board[row][i] == num:
            return False
        
    for i in range(len(board)):
        if board[i][col] == num:
            return False
        
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3
    
    for i in range(3):
        curRow = rowStart + i
        for j in range(3):
            curCol = colStart + j
            if board[curRow][curCol] == num:
                return False
    
    return True

def getEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                return i, j
            

board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(sudokuSolver(board))