# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

# Time O(n) | Space O(n)
def buildTree(preorder, postorder):
    if not preorder or not postorder:
        return 
    
    if len(preorder) == 1:
        return TreeNode(postorder.pop())
    
    root = TreeNode(postorder.pop())
    mid = preorder.index(postorder[-1])
    
    root.right = buildTree(preorder[mid:], postorder)
    root.left = buildTree(preorder[1:mid], postorder)
    
    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
