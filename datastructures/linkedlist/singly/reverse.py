class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while (current is not None):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    def reverse_recursive(self):
        if self.head is None:
            return
        self.reverse_util(self.head, None)

    def reverse_util(self, current, previous):
        if current.next is None:
            self.head = current
            current.next = previous
            return
        next = current.next
        current.next = previous
        self.reverse_util(next, current)           

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist.print_list()

llist.reverse_recursive()
llist.print_list()