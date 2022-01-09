
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def top(self):
        if self.isEmpty():
            raise Exception("Stack Empty")

        return self.head.next.val

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Empty")

        nodeToremove = self.head.next
        self.head.next = self.head.next.next 
        self.size -= 1
        return nodeToremove.val
