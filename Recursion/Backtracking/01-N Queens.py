# You are given a N * N Chess board, find out how many ways we can place N Queens such that no queens are eliminating the other Queens

# TIme O(N^3 + N!) | Space O(N^2)
def NQueens(board, row):
    if row == len(board):
        display(board)
        print()
        return 1
    
    count = 0
    # placing Queen and checking for every row and col
    for col in range(0, len(board)):
        # place the queen if there is no line of sight of other Queens which are already placed
        if isSafe(board, row, col):
            board[row][col] = True
            count += NQueens(board, row + 1)
            board[row][col] = False

    return count

def isSafe(board, row, col):
    # check vertical 
    for i in range(row):
        if board[i][col]:
            return False
        
    # diagonal left
    maxLeft = min(row, col)
    for i in range(1, maxLeft + 1):
        if board[row - i][col - i]:
            return False

    # diagonal right
    maxRight = min(row, len(board) - col - 1)
    for i in range(1, maxRight + 1):
        if board[row - i][col + i]:
            return False

    return True

def display(board):
    for row in board:
        for ele in row:
            if ele:
                print("Q", end=" ")
            else:
                print("x", end=" ")
        print()


# board = [   
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False]
# ]

# print(NQueens(board, 0))
    

