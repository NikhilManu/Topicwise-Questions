# https://leetcode.com/problems/palindrome-linked-list

# Time O(N) | Space O(1)
def isPalindrome(head):
    mid = MiddleNode(head)    
    tail = reverseList(mid)
    while head and tail: # Actually we only need to use tail, since tail is always greater than or equal to head
        if head.val != tail.val:
            return False
        
        head = head.next
        tail = tail.next
        
    return True

# Time O(N) | Space O(1)
def reverseList(head):
    newHead = None
    while head:
        head.next, newHead, head = newHead, head, head.next
        
    return newHead

# Time O(N) | Space O(1)
def MiddleNode(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow