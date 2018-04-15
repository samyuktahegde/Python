class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node        
        self.head = new_node

    def is_circular(self):
        temp = self.head
        while temp.next is not None and temp.next!=self.head:
            temp = temp.next
        print(temp.data)
        return temp.next==self.head

clist = CircularLinkedList()
clist.push(1)
clist.push(2)
clist.push(3)
# clist.print_list()

print(clist.is_circular())