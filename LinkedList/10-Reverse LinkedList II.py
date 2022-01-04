# https://leetcode.com/problems/reverse-linked-list-ii/

# Single Pass Solution
# Time O(N) | Space O(1)
def Reverse(head, left, right):
    if left == right:
        return head

    dummy = prev = ListNode()
    prev.next = head

    for _ in range(1, left):
        prev = prev.next

    cur = prev.next
    while left < right:
        temp = cur.next
        cur.next = temp.next
        temp.next = prev.next 
        prev.next = temp
        left += 1

    return dummy.next 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next