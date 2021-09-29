# https://leetcode.com/problems/find-a-peak-element-ii/

# Time O(n logm) | Space O(1)
def findPeakGrid(mat):
    """
    How is Binary Search possible here?
    First we should understand that this is a Greedy Problem.
    
    Say we took the largest element in a column, if any of adjacent
    element is greater than the current Largest, we can just greedily go through
    the largest elements till we find a Peak Element
    
    In my Solution I am splitting column wise because in the hint it is given that width
    is more that the height.
    """
    start, end = 0, len(mat[0]) - 1
    while start <= end:
        cmid = start + (end - start) // 2
        
        # Finding the largest element in the middle Column
        ridx, curLargest = 0, float('-inf')
        for i in range(len(mat)):
            if mat[i][cmid] > curLargest:
                curLargest = mat[i][cmid]
                ridx= i 
        
        # Checking the adjacent element
        leftisBig = cmid > start and mat[ridx][cmid - 1] > mat[ridx][cmid]
        rightisBig = cmid < end and mat[ridx][cmid + 1] > mat[ridx][cmid]
        
        if not leftisBig and not rightisBig:
            return [ridx, cmid]
        
        if leftisBig:
            end = cmid - 1
        else:
            start = cmid + 1