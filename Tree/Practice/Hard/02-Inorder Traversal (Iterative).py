# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Time O(N) | Space O(1) if resultant array is not included
def MorrisTraversal(root):
    cur, res = root, []
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            pred = cur.left
            while pred.right and pred.right != cur:
                pred = pred.right
            
            if not pred.right:
                pred.right = cur
                cur = cur.left
            else:
                res.append(cur.val)
                pred.right = None
                cur = cur.right
    return res

"""
logic: 
        At every node which doesnt have a left child we have find that nodes inorder predecessor and connect the predecessor's right to
        current node 
        So after every node which doesnt have a left child, just append the value of that node and we can just go to the right child of that 
        node since we already connected its right with it inorder successor 
"""