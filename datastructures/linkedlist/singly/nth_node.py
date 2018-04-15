class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_n_from_last(self, n):
        temp = self.head
        length=0
        while temp:
            length=length+1
            temp=temp.next
        # print(length)
        if n>length:
            return
        temp = self.head
        # print(n)
        node_index = length-n-1
        # print('ll'+str(node_index))
        for i in range(0, node_index):
            temp = temp.next
        print(temp.data)


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
llist.print_n_from_last(3)