# Reach end of matrix, there are some obstacles on some [r, c]

# returns all the path
def pathRestriction(maze, row, col, cur):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        return [cur]

    if not maze[row][col]:
        return []

    path = []
    if row < len(maze) - 1:
        path.extend(pathRestriction(maze, row + 1, col, cur + 'D'))
    
    if col < len(maze[0]) - 1:
        path.extend(pathRestriction(maze, row, col + 1, cur + 'R'))

    return path


# Can go all direction
def pathRestrictionII(maze, row, col, cur):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        return [cur]

    if not maze[row][col]:
        return []

    maze[row][col] = False # We make it false because we dont want to revisit this node in current recursive call

    path = []
    if row < len(maze) - 1:
        path.extend(pathRestrictionII(maze, row + 1, col, cur + 'D'))
    
    if col < len(maze[0]) - 1:
        path.extend(pathRestrictionII(maze, row, col + 1, cur + 'R'))

    if row > 0:
        path.extend(pathRestrictionII(maze, row - 1, col, cur + 'U'))

    if col > 0:
        path.extend(pathRestrictionII(maze, row, col - 1, cur + 'L'))

    maze[row][col] = True # We revert the changes we made before exiting from the current recursive call
    return path


# maze = [   
#     [True, True, True],
#     [True, True, True],
#     [True, True, True]
# ]

# print(pathRestrictionII(maze, 0, 0, ""))