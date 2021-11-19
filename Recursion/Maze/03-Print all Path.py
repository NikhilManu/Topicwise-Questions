# Reach end of matrix, there are some obstacles on some [r, c]
# print all the ways in the maze by which we can start and end

# Can go all direction
def allPathPrint(maze, row, col, cur, path, step):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        path[row][col] = step
        for arr in path:
            print(arr)

        print(cur)
        print()

    if not maze[row][col]:
        return 

    maze[row][col] = False # We make it false because we dont want to revisit this node in current recursive call
    path[row][col] = step
    if row < len(maze) - 1:
        allPathPrint(maze, row + 1, col, cur + 'D', path, step + 1)
    
    if col < len(maze[0]) - 1:
        allPathPrint(maze, row, col + 1, cur + 'R', path, step + 1)

    if row > 0:
        allPathPrint(maze, row - 1, col, cur + 'U', path, step + 1)

    if col > 0:
        allPathPrint(maze, row, col - 1, cur + 'L', path, step + 1)

    maze[row][col] = True # We revert the changes we made before exiting from the current recursive call
    path[row][col] = 0

    return path


# Test case 
# maze = [   
#     [True, True, True],
#     [True, True, True],
#     [True, True, True]
# ]

# path = [   
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# allPathPrint(maze, 0, 0, "", path, 1)