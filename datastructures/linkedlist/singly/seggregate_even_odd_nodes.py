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
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def segregate_even_odd(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        last_node = temp
        oddlist = LinkedList()
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data%2 != 0:
                oddlist.append(temp.data)
                if temp == self.head:
                    self.head = temp.next
                    prev = self.head
                else:
                    prev.next = temp.next
                    prev = temp
            temp = temp.next
            # print(temp.data)
        self.print_list()
        oddlist.print_list()
        


                 
            


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
# llist.print_list()
llist.segregate_even_odd()
