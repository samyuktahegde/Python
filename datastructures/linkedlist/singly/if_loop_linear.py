class Node:
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

    # def detect_loop(self):
    #     s = set()
    #     temp = self.head
    #     while(temp):
    #         if temp in s:
    #             return True
    #         s.add(temp)
    #         temp = temp.next        
    #     return False

    def detect_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
            if slow_pointer == fast_pointer:
                print ('Found Loop')
                return
            
        
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist.print_list()
print(llist.detect_loop())

llist.head.next.next.next.next = llist.head;
print(llist.detect_loop())
