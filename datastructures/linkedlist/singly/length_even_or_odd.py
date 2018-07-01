class  Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def length_even_or_odd(self):
        temp = llist.head
        while temp is not None and temp.next is not None:
            temp = temp.next.next
        if temp is None:
            return 'Even Length'
        else:
            return 'Odd Length'

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.print_list()
print(llist.length_even_or_odd())