# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Time O(N) | Space O(1)
def flattenTree(root):
    cur = root
    while cur:
        if cur.left:
            pred = cur.left
            while pred.right:
                pred = pred.right
            
            pred.right = cur.right
            cur.right = cur.left
            cur.left = None

        cur = cur.right
"""
For every node with left tree, we find its inorder Predecessor,
we make pred right sub tree as the node's right sub tree and 
then we make node right sub tree as node's left sutree
then we make the node's left subtree as null

Initial Tree:
					    1
					   / \
					  2   5
					 / \   \
					3   4   6
Then,
				        1
					   / 
					  2   
					 / \   
					3   4   
					      \
						   5
						    \
						     6
Then,
						1
						  \
						    2   
						   /  \   
						  3    4   
						     	 \
                                   5
                                    \
                                     6
Then:
						1
						  \
						   2   
						   /     
						  3    
                            \
						     4   
                              \
							   5
							    \
							     6
Then:
						1
						  \
						    2
						      \
						        3    
							     \
                                  4   
								    \
                                    5
								     \
								       6
"""