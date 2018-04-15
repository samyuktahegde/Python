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

    def check_palindrome(self):
        current = self.head
        stack = []
        while current is not None:
            stack.append(current.data)
            current = current.next
        n = len(stack)
        for i in range(n):
            if stack[i] != stack[n-1-i]:
                return False
        return True

llist = LinkedList()
llist.push(11)
llist.push(20)
llist.push(13)
llist.push(13)
llist.push(20)
llist.push(13)
llist.print_list()
print(llist.check_palindrome())
