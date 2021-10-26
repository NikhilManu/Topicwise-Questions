"""
A Right Sibling Tree is obtained by making every node in a Binary Tree have its right property point to its immediate right Node on the 
same lever or Null if there is no immediate node to its right.

Note: After transformation some node can be completly unreachable.

Transformation should be done in Place

             1
          /     \   
        2         3      
      /  \        /\
    4     5      6   7
  /  \     \     /   /\
 8    9     10  11  12 13
                /
               14


             1 -->
          /        
        2 -->     3      
      /           /
    4 --> 5  --> 6-->7
  /             /   /
 8 -->9    10-->11 12-->13
                /
               14
"""


# Time O(N) | Space O(d)
def rightSiblingTree(root):
	helper(root, None, False)
	return root

def helper(node, parent, isLeft):
	if not node:
		return 
	
	left, right = node.left, node.right
	helper(left, node, True)
	if not parent:
		node.right = None
	elif isLeft:
		node.right = parent.right
	else:
		if not parent.right:
			node.right = None
		else:
			node.right = parent.right.left
	helper(right, node, False)


"""
Logic if finding the pattern of a node.
    1. if cur node is a left child: 
            change the curnode-> right to parent->right
    2. if cur node is a right child:
            change the curnode->right to parent->right->left
            (this is possible because we are changing the pointer while traversing)
"""