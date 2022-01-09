
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        node = Node(value)

        if self.isEmpty():
            self.front = self.rear = node
            self.size += 1
            return 

        self.rear.next = node
        self.rear = node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Empty")

        node = self.front
        self.front = node.next

        if not self.front:
            self.rear = None

        self.size -= 1
        return node.val