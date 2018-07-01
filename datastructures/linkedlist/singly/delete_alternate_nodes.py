class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete_alternate_nodes(self):
        temp = self.head
        while temp is not None and temp.next is not None and temp.next.next is not None:
            temp.next = temp.next.next
            temp = temp.next
        if temp is not None:
            temp.next = None

llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
# llist.push(2)

llist.print_list()
print('-------------------------------------')
llist.delete_alternate_nodes()
# llist.sort_list()
llist.print_list()