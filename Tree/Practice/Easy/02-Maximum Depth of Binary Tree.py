# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Time O(N) | Space O(N)
def maxDepth(root):
    if not root:
        return 0
    
    l = maxDepth(root.left)
    r = maxDepth(root.right)
    return 1 + max(l, r)