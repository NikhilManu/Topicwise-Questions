# https://leetcode.com/problems/reverse-nodes-in-k-group

# First Look Reverse LinkedList II

# Time O(N) | Space O(1)
def reverseKGroup(head, k):
    if not head or k == 1:
        return head
        
    length = getLength(head) # I had to find length since I couldnt come up with a way without It.
    
    dummy = prev = ListNode()
    prev.next = head
    
    i = 0
    while i < length // k:
        
        cur = prev.next

        # Same as reverse LinkedList II Logic
        for _ in range(k - 1):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next 
            prev.next = temp
            
        
        prev = cur
        i += 1
                
        return dummy.next
    
def getLength(head):
    l = 1
    while head.next:
        head = head.next
        l += 1
        
    return l

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next