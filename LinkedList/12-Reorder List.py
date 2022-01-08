# https://leetcode.com/problems/reorder-list/

# Time O(N) | Space O(1)
def reorderList(head):
    if not head or not head.next:
        return head
    
    mid = MiddleNode(head)
    tail = reverseList(mid)
    dummy = cur = ListNode()
    while head and tail:
        cur.next = head
        head = head.next
        cur = cur.next
        
        cur.next = tail
        tail = tail.next
        cur = cur.next
        
    cur.next = tail
    return dummy.next

# Time O(N) | Space O(1)
def reverseList(head):
    newHead = None
    while head:
        head.next, newHead, head = newHead, head, head.next
        
    return newHead

# Time O(N) | Space O(1)
def MiddleNode(head):
    slow, fast = head, head
    tmp = None
    while fast and fast.next:
        tmp = slow
        slow = slow.next
        fast = fast.next.next
    
    tmp.next = None
    return slow

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next