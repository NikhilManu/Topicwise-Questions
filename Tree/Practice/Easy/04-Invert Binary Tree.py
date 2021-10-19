# https://leetcode.com/problems/invert-binary-tree

# Time O(n) | O(h) Space
def invertTree(root):
    if not root:
        return
    
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root

# Time O(n) | Space O(n)
def invertTree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        
        if not node:
            continue
        
        node.left, node.right = node.right, node.left
        
        stack.append(node.left)
        stack.append(node.right)
        
    return root