class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_linked_list(self):
        temp = self.head
        while temp:
            next = temp.next
            temp.data = None
            temp.next = None
            temp = next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth

llist.delete_linked_list()
print(second.data)
