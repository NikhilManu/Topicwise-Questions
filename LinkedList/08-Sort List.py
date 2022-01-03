# https://leetcode.com/problems/sort-list/

# O(NlogN) | Space O(logN)
def sortList(head):
    if not head or not head.next:
        return head

    mid = MiddleNode(head)
    left = sortList(head)
    right = sortList(mid)

    return mergeSortedList(left, right)

def mergeSortedList(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    
    head = ListNode(-1)
    node = head
    
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
            
        node = node.next
        
    node.next = list1 or list2
        
    return head.next

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
    def __init__(self, val, node = None):
        self.val = val
        self.next = node