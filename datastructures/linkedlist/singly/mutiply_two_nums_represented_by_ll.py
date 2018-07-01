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

def multiply(list1, list2):
    number1 = 0
    number2 = 0
    temp1 = list1.head
    temp2 = list2.head
    while temp1 is not None:
        number1=number1*10+temp1.data
        temp1 = temp1.next
    while temp2 is not None:
        number2=number2*10+temp2.data
        temp2 = temp2.next
    return number1*number2
    
llist1 = LinkedList()
llist1.push(1)
llist1.push(2)
llist1.push(3)
llist1.print_list()

llist2 = LinkedList()
llist2.push(2)
llist2.push(1)
llist2.print_list()

print(multiply(llist1, llist2))