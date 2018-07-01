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

    def add_two_numbers(self, llist1, llist2):
        first = llist1.head
        second = llist2.head
        carry = 0
        prev = None
        temp = None
        while first is not None or second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            sum = fdata+sdata+carry
            carry = 1 if sum>=10 else 0
            sum = sum if sum<10 else sum%10

            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

first = LinkedList()
second = LinkedList()
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
first.print_list()
print('-------------------------------------')
second.push(4)
second.push(8)
second.print_list()
print('-------------------------------------')
result = LinkedList()
result.add_two_numbers(first, second)
result.print_list()
            
                
        
        
