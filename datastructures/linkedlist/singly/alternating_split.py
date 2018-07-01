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

def alternating_split(llist):
    odd = LinkedList()
    even = LinkedList()
    temp = llist.head
    i=1
    while temp is not None:
        if i%2 == 0:
            even.push(temp.data)
        else:
            odd.push(temp.data)
        i+=1
        temp = temp.next
    odd.print_list()
    print('-------------------------------------')
    even.print_list()

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
alternating_split(llist)

    
        
