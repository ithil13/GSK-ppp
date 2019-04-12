class Node:
    def __init__(self, data=None, neext=None):
        self.data = data
        self.next = neext 

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def pop(self):
        value = self.head.data
        if self.head.next != None:
            self.head = self.head.next
        else:
            self.head = None
        self.size -= 1
        return value

    def is_empty(self):
        return self.size == 0