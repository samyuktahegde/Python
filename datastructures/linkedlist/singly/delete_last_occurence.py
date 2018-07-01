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

    def delete_last_occurence(self, key):
        temp = self.head
        last_key_match = None
        while temp is not None:
            if temp.data == key:
                last_key_match = temp
            temp = temp.next

        if last_key_match is not None and last_key_match.next is None:
            temp = self.head
            while temp.next != last_key_match:
                temp = temp.next
            temp.next = None

        if last_key_match is not None and last_key_match.next is not None:
            last_key_match.data = last_key_match.next.data
            last_key_match.next = last_key_match.next.next

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
llist.delete_last_occurence(0)
# llist.sort_list()
llist.print_list()
