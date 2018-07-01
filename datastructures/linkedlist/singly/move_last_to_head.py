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
    
    def push_last_to_first(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
       
        new_head = temp.next
        # print(new_head.data)
        temp.next = None
        # print(temp.data)
        new_head.next = self.head
        # print(new_head.next.data)
        self.head = new_head


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.print_list()
print('-------------------------------------')
llist.push_last_to_first()
llist.print_list()