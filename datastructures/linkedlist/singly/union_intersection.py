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

def get_intersection(list1, list2):
    list1_set = []
    intersection = []
    temp1 = list1.head
    while temp1 is not None:
        list1_set.append(temp1.data)
        temp1 = temp1.next
    temp2 = list2.head
    while temp2 is not None:
        if temp2.data in list1_set:
            intersection.append(temp2.data)
        temp2 = temp2.next
    return intersection

def get_union(list1, list2):
    union = []
    temp1 = list1.head
    while temp1 is not None:
        union.append(temp1.data)
        temp1 = temp1.next
    temp2 = list2.head
    while temp2 is not None:
        if not temp2.data in union:
            union.append(temp2.data)
        temp2 = temp2.next
    return union

llist1 = LinkedList()
llist1.push(1)
llist1.push(2)

llist2 = LinkedList()
llist2.push(3)
llist2.push(2)

print(get_intersection(llist1, llist2))
print(get_union(llist1, llist2))
    
    
