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

    def sum_last_n(self, n):
        l_length = 0
        temp = llist.head
        stack = []
        while temp is not None:
            l_length+=1
            stack.append(temp.data)
            temp = temp.next
        sum = 0
        while n>0:
            sum+=stack.pop()
            n-=1
        return sum
        

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.print_list()
print(llist.sum_last_n(3))