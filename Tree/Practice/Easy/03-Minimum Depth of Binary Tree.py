# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Solution 1 --> DFS Traverses the entire tree, which is waste of time
# Time O(N) | Space O(h)

def minDepth(root):
    return helper(root) if root else 0

def helper(root):
    if not root:
        return float('inf')

    left = helper(root.left)
    right = helper(root.right)

    if not root.left and not root.right:
        return 1
    
    return min(left, right) + 1

# Solution 2 --> BFS
# Time O(N) | Space O(h)
def minDepth(root):
    if not root:
        return 0

    queue = Deque([(root, 1)]) #Queue
    while queue:
        node, depth = queue.pop()

        if not node.left and not node.right:
            return depth 
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0