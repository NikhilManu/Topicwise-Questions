# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Time O(N^2) | Space O(N)

# This Solution is n^2 because take example case of 
# 1, 2, 3, ..., N    Here the number of Operations is N^2
def buildBST(preorder):
    if not preorder:
        return 
    
    rootVal = preorder[0]
    greater, smaller = [], []
    for num in preorder[1:]:
        if num > rootVal:
            greater.append(num)
        else:
            smaller.append(num)
            
    root = TreeNode(rootVal)
    root.left = buildBST(smaller)
    root.right = buildBST(greater)
    
    return root

# Time O(N) | Space O(N)
i = 0
def buildBST(preorder):
    return helper(preorder, float('-inf'), float('inf'))

def helper(preorder, start, end):
    if i == len(preorder) or preorder[i] < start or preorder[i] > end:
        return 
    
    root = TreeNode(preorder[i])
    i += 1
    root.left = helper(preorder, start, root.val)
    root.right = helper(preorder, root.val, end)
    
    return root

# Time O(N) | Space O(N)
# We only take the Upper Bound
i = 0
def buildBST(preorder):
    return helper(preorder, float('inf'))

def helper(preorder, bound):
    if i == len(preorder) or preorder[i] > bound:
        return 
    
    root = TreeNode(preorder[i])
    i += 1
    root.left = helper(preorder, root.val)
    root.right = helper(preorder, bound)
    
    return root