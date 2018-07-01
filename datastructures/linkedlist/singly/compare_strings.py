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

def compare(list1, list2):
    temp1 = list1.head
    temp2 = list2.head

    while temp1 is not None and temp2 is not None and temp1.data==temp2.data:
        temp1=temp1.next
        temp2=temp2.next
    
    if temp1 and temp2:
        return 1 if temp1.data > temp2.data else -1
    if temp1 and not temp2:
        return 1
    if temp2 and not temp1:
        return -1
    return 0

list1 = LinkedList()
list1.push('a')
list1.push('s')
list1.push('k')
list1.push('e')
list1.push('e')
list1.push('g')

 
list2 = LinkedList() 
list2.push('a')
list2.push('s')
list2.push('k')
list2.push('e')
list2.push('e')
list2.push('g')

print(compare(list1, list2))
