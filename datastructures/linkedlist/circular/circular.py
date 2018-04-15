class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node        
        self.head = new_node

    def print_list(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print ("%d" %(temp.data))
                temp = temp.next
                if (temp == self.head):
                    break

    def split_list(self, head1, head2):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is None:
            return
        while(fast_ptr.next!= self.head and fast_ptr.next.next!=self.head):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next
        head1.head = self.head
        if self.head.next != self.head:
            head2.head = slow_ptr.next
        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head
        

# clist = CircularLinkedList()
# clist.push(1)
# clist.push(2)
# clist.push(3)
# clist.print_list()


head = CircularLinkedList() 
head1 = CircularLinkedList()
head2 = CircularLinkedList()
 
head.push(12)
head.push(56)
head.push(2)
head.push(11)
 
print ("Original Circular Linked List")
head.print_list()
 
# Split the list 
head.split_list(head1 , head2)
 
print ("\nFirst Circular Linked List")
head1.print_list()
 
print ("\nSecond Circular Linked List")
head2.print_list()
