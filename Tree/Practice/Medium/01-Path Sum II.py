# https://leetcode.com/problems/path-sum-ii

# Time O(N) | Space O(N)
def PathSumII(root, targetSum):
    res = []
    helper(root, targetSum, 0, [], res)
    return res

def helper(node, targetSum, curSum, path, res):
    if not node:
        return

    curSum += node.val
    path.append(node.val)
    if not node.left and not node.right and curSum == targetSum:
        res.append(path[:]) # Remember to append the copy of path

    helper(node.left, targetSum, curSum, path, res)
    helper(node.right, targetSum, curSum, path, res)
    path.pop()