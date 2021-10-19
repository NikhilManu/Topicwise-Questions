# Not LC Qn
# Find the inorder Successor of Binary Tree. (dot)parent points to parent node of the current child

# Time O(N) | Space O(1)
def findSucc(root, node):
    if node.right:
        return findSuccFromRight(node)

    return findSuccFromAbove(node)

def findSuccFromRight(node):
    succ = node.right
    while succ.left:
        succ = succ.left

    return succ

# we have to traverse till the current node is in leftsubtree of the parent.
def findSuccFromAbove(node):
    parent = node.parent
    cur = node
    while parent and parent.right == cur:
        cur = parent
        parent = parent.parent

    return parent
