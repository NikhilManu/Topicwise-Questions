# You are given a N * N Chess board, find out how many ways we can place N Knights such that no knights are eliminating the other Knights

def NKnights(board, row, col, knights):
    if knights == 0:
        display(board)
        print()
        return 

    if row == len(board) - 1 and col == len(board):
        return 

    if col == len(board):
        NKnights(board, row + 1, 0, knights)
        return

    if isSafe(board, row, col):
        board[row][col] = True
        NKnights(board, row, col + 1, knights - 1)
        board[row][col] = False

    NKnights(board, row, col + 1, knights)

def isSafe(board, row, col):
    if isValid(board, row - 2, col - 1):
        if board[row - 2][col - 1]:
            return False

    if isValid(board, row - 2, col + 1):
        if board[row - 2][col + 1]:
            return False

    if isValid(board, row - 1, col - 2):
        if board[row - 1][col - 2]:
            return False

    if isValid(board, row - 1, col - 2):
        if board[row - 1][col - 2]:
            return False

    return True

def isValid(board, row, col):
    return row >= 0 and row < len(board) and col >= 0 and col < len(board)

def display(board):
    for row in board:
        for ele in row:
            if ele:
                print("K", end=" ")
            else:
                print("x", end=" ")
        print()


board = [   
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

NKnights(board, 0, 0, 4)

