# https://leetcode.com/problems/linked-list-cycle-ii

# Time O(N) | Space O(1)
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            while head != slow:
                    head = head.next
                    slow = slow.next
                    
            return slow
    
    return None