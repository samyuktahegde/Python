class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def detect_and_remove_loop(self):
        slow_pointer = fast_pointer = self.head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer==fast_pointer:
                self.remove_loop(slow_pointer)
                return 1
        return 0

    def remove_loop(self, loop_node):
        pointer1 = self.head
        while 1:
            pointer2 = loop_node
            while pointer2.next!=loop_node and pointer2.next!=pointer1:
                pointer2 = pointer2.next
            if pointer2.next == pointer1:
                break
            pointer1 = pointer1.next
