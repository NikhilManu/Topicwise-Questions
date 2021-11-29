# 

# 
def WordSearch(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and check(board, word, 0, set(), i, j):
                return True
            
    return False

def check(board, word, idx, vis, i, j):
    if idx == len(word):
        return True
    
    if outOfBounds(i, j, board) or (i, j) in vis or board[i][j] != word[idx]:
        return False
    
    vis.add((i, j))
    left = check(board, word, idx + 1, vis, i, j - 1)
    right = check(board, word, idx + 1, vis, i, j + 1)
    up = check(board, word, idx + 1, vis, i - 1, j)
    down = check(board, word, idx + 1, vis, i + 1, j)
    vis.remove((i, j))
    
    return left or right or up or down

def outOfBounds(i, j, board):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) 