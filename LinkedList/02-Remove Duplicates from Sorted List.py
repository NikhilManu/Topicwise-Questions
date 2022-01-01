# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Time O(N) | Space O(1)
def DeleteDups(head):
    node = head
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
            
    return head