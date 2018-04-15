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

    def remove_duplicates(self):
        current = self.head
        while current.next is not None:
            next_node = current.next
            next_next_node = next_node.next
            if current.data == next_node.data:
                current.next = next_next_node
            else:
                current = current.next

    def remove_duplicates_unordered(self):
        current = self.head
        linkedlist_set = []
        if current is not None:
            linkedlist_set.append(current.data)
        else:
            return
        while current.next is not None:
            next_node = current.next
            next_next_node = next_node.next
            if not next_node.data in linkedlist_set:
                linkedlist_set.append(next_node.data)
                current = current.next
            else:
                current.next = next_next_node


llist = LinkedList()
llist.push(11)
llist.push(20)
llist.push(13)
llist.push(11)
llist.push(13)
llist.push(11)
llist.print_list()
llist.remove_duplicates_unordered()
print('---------------------------------------')
llist.print_list()