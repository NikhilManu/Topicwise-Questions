# https://leetcode.com/problems/reverse-linked-list

# Time O(N) | Space O(1)
def reverseList(head):
    newHead = None
    while head:
        tmp  = head.next
        head.next = newHead
        newHead = head
        head = tmp
        
    return newHead

# Time O(N) | Space O(1)
def reverseList(head):
    newHead = None
    while head:
        head.next, newHead, head = newHead, head, head.next
        
    return newHead

# Time O(N) | Space O(N)
def reverseList(head):
    if not head or not head.next:
        return head
    
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead
