# 

def Insert(head, val, index): # Here index denotes how many index away from insert position
    head = insertRec(val, index, head)
    return head

def insertRec(val, index, node):
    if index == 0:
        temp = Node(val, node)
        return temp # we return the node to be inserted if index == 0

    node.next = insertRec(val, index - 1, node.next)
    return node

class Node:
    def __init__(self, val, node):
        self.val = val
        self.next = node