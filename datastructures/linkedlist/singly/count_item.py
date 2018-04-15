class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def count(self, search_item):
        temp = self.head
        count = 0
        while temp:
            if temp.data == search_item:
                count=count+1
            temp = temp.next
        return count

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth
fourth.next = Node(2)
fourth.next.next = Node(2)
print(llist.count(2))
