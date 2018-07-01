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

def triplet(a, b, c, given_number):
    tempA = a.head
    while tempA is not None:
        tempB = b.head
        tempC = c.head
        while tempB is not None and tempC is not None:
            sum = tempA.data+tempB.data+tempC.data
            if sum==given_number:
                print(tempA.data, tempB.data, tempC.data)
                return
            elif sum<given_number:
                tempB = tempB.next
            else:
                tempC=tempC.next
        tempA=tempA.next

llist1 = LinkedList()
llist1.push(20)
llist1.push(4)
llist1.push(15)
llist1.push(10)
llist1.print_list()

print('-------------------------------------')
llist2 = LinkedList()
llist2.push(10)
llist2.push(9)
llist2.push(4)
llist2.push(2)
llist2.print_list()

print('-------------------------------------')
llist3 = LinkedList()
llist3.push(1)
llist3.push(2)
llist3.push(4)
llist3.push(8)
llist3.print_list()

print('-------------------------------------')
triplet(llist1, llist2, llist3, 25)
