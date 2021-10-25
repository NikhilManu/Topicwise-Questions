# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Time O(N) | Space O(N)
def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return
    
    rootVal = postorder.pop()
    
    root = TreeNode(rootVal)
    mid = inorder.index(rootVal)
    
    # indices can be passed to be improved
    root.right = buildTree(inorder[mid + 1:], postorder) 
    root.left = buildTree(inorder[:mid], postorder)
    
    
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right