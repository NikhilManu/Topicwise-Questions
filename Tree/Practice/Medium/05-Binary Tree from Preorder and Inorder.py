# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Time O(n) | Space O(n)
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return 
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
    
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
For Improving the solution we can pass the index of arrays rather than slicing the array
"""