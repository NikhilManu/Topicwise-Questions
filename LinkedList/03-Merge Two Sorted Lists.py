# https://leetcode.com/problems/merge-two-sorted-lists

# Time O(N) | Spcae O(1)
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


class ListNode:
    def __init__(self, val, node = None):
        self.val = val
        self.next = node
        