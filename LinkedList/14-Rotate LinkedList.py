# https://leetcode.com/problems/rotate-list/

# Time O(N) | Space O(1)
def rotateRight(head, k):
    if not head or k == 0:
        return head
    
    length = getLength(head)
    k = k % length
    
    if k == 0:
        return head
    
    first = second = head
    for _ in range(k):
        first = first.next
        
    while first.next:
        first = first.next
        second = second.next
        
    newHead = second.next
    second.next = None
    first.next = head
    
    return newHead
        
    
def getLength(node):
    l = 1
    while node.next:
        node = node.next
        l += 1
        
    return l