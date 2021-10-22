# https://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/

# Time O(N) | Space O(d) where d is depth of tree
def ConvertToDLL(root):
    leftMost, _ = helper(root)
    return leftMost

def helper(node):
    if not node.left:
        leftMost = node
    else:
        LeftTreeLeftMost, LeftTreeRightMost = helper(node.left)
        LeftTreeRightMost.right = node
        node.left = LeftTreeRightMost
        leftMost = LeftTreeLeftMost

    if not node.right:
        rightMost = node
    else:
        RightTreeLeftMost, RightTreeRightMost = helper(node.right)
        RightTreeLeftMost.left = node
        node.right = RightTreeLeftMost
        rightMost = RightTreeRightMost

    return leftMost, rightMost

"""
Logic:
    at any node we need to find the inorder Successor and inorder Predecessor of that node

    Inorder Successor is right subtree's leftMost child
    Inorder Predecessor is left subtree's rightMost child
"""