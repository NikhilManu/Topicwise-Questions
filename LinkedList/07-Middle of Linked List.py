# https://leetcode.com/problems/middle-of-the-linked-list

# Solution 1
# Time O(N) | Space O(1)
def MiddleNode(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow