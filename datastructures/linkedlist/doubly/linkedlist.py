class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
