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

    def sort_list(self):
        temp = self.head
        count = [0, 0, 0]
        while temp is not None:
            count[temp.data]+=1
            temp = temp.next
        
        temp = self.head
        for c in range(len(count)):
            for i in range(count[c]):
                temp.data = c
                temp = temp.next
        
llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)

llist.print_list()
print('-------------------------------------')
llist.sort_list()
llist.print_list()