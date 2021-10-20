# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# O(N) Time | O(d) Space
def MaxPathSum(root):
    _, maxPathSum = helper(root)
    return maxPathSum

def helper(node):
    if not node:
        return 0, float('-inf')
    
    left, leftMaxPathSum = helper(node.left)
    right, rightMaxPathSum = helper(node.right)
    
    maxBranch = max(left, right)  + node.val
    maxatNode = max(node.val, left + node.val + right, maxBranch)
    curMaxPathSum = max(maxatNode, leftMaxPathSum, rightMaxPathSum)
    
    return maxBranch, curMaxPathSum


"""
The logic is similar to Diameter of Binary Tree. 

At any node the maxpathsum of that node 
        --> can be the current node only (consider a node which is positive and all other node are negative)
        --> can be leftSubTree + current node
        --> can be rightSubTree + current node
        --> can be leftSubTree + current node + rightSubTree
        --> can be on the leftSubTree (ie. maxpathsum already found on left subtree)
        --> can be on the RightSubTree (ie. maxpathsum already found on right subtree)
"""