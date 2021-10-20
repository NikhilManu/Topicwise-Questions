import collections
# 

# Time O(N) | Space O(N)
def KDistance(root, target, k):
    parent = getParent(root)
    
    res, visited = [], set([target])
    queue = collections.deque([target])
    # BFS
    while queue and k >= 0:
        for _ in range(len(queue)):
            node = queue.popleft()
            
            if k == 0:
                res.append(node.val)
            
            if node.left and node.left not in visited:
                queue.append(node.left)
                visited.add(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
                visited.add(node.right)
            if parent[node] and parent[node] not in visited:
                queue.append(parent[node])
                visited.add(parent[node])
                
        k -= 1
                
    return res
    
def getParent(root):
    parent = {root:None}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
            
    return parent


"""
BFS is more effiecent than dfs in this case,

Logic here is simple, just add all the neighbouring elements to the queue and mark the node as visited
when the nodes are at kth distance from node just append them to a list
"""