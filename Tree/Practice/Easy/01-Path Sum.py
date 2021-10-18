# https://leetcode.com/problems/path-sum

# Time O(N) | Space O(N) where N is the no of nodes in Tree
def PathSum(root, targetSum):
    return helper(root, targetSum, 0)

def helper(root, targetSum, curSum):
    if not root:
        return 
    
    curSum += root.val
    if not root.right and not root.left:
        return curSum == targetSum

    return helper(root.left, targetSum, curSum) or helper(root.right, targetSum, curSum)