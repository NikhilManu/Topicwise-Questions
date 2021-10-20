# https://leetcode.com/problems/balanced-binary-tree

# Time O(N) | Space O(h)
def isBalanced(root):
    _, isBalanced = helper(root)
    return isBalanced

def helper(root):
    if not root:
        return 0, True
    
    left, isLeftBalanced = helper(root.left) 
    right, isRightBalanced = helper(root.right)
    
    if not isLeftBalanced or not isRightBalanced:
        return -1, False
        
        
    curMaxTree = max(left, right) + 1
    isBalanced = True if abs(left - right) <= 1 else False
    
    return curMaxTree, isBalanced

"""
Logic similar to Qn 05
At any node, we check whether
        --> any of leftSubtree was unbalanced
        --> any of right Subtree was unbalanced
        --> if our current node is unbalanced
"""