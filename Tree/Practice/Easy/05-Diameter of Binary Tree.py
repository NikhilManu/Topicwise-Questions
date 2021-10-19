# https://leetcode.com/problems/diameter-of-binary-tree

# Time O(N) | Space O(d)
def Diameter(root):
    _, diameter = helper(root)
    return diameter

def helper(root):
    if not root:
        return 0, 0

    leftMax, leftDia = helper(root.left)
    rightMax, rightDia = helper(root.right)

    curMaxSubTree = 1 + max(leftMax, rightMax)
    maxDiameter = max(leftMax + rightMax, leftDia, rightDia)

    return curMaxSubTree, maxDiameter

"""
The logics here is, 
    - At any node, maxDiameter of that node can be 
            --> largest diameter occured on the leftSub Tree of that node, OR
            --> largest diameter which occured on the RightSub Tree of that node, OR
            --> current node that we are standing, ie.. leftsubtree + rightSubtree 

            leftSubTree + rightSubTree + 1 is not required since in the qn it is asked path, if the qn 
            was no of nodes we would have needed the +1
"""