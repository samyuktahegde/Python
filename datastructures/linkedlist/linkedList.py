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
            print temp.data
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print "The given previous node must be in the LinkedList."
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp==None:
            return

        prev.next = temp.next
        temp = None

    def delete_node_position(self, position):
        if self.head == None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def get_count(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count

    def find_middle(self):
        slow_temp = self.head
        fast_temp = self.head
        while fast_temp != None and fast_temp.next != None:
            fast_temp = fast_temp.next.next
            slow_temp = slow_temp.next
        return slow_temp.data

    # def search(self, x):
    #     temp = self.head
    #     while temp != None:
    #         if temp.data == x:
    #             return True
    #         temp = temp.next
    #     return False

    def search(self, temp_head, x):
        if temp_head == None:
            return False
        if temp_head.data == x:
            return True
        return self.search(temp_head.next, x)

    def swap_nodes(self, x, y):
        if x == y:
            return
        prev_x = None
        curr_x = self.head
        while curr_x != None and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next
        # print curr_x.data
        prev_y = None
        curr_y = self.head
        while curr_y != None and curr_y.data != y:
            prev_y = curr_y
            curr_y = curr_y.next
        # print curr_y.data
        if curr_x == None or curr_y == None:
            return
        if prev_x != None:
            prev_x.next = curr_y
        else:
            self.head = curr_y
        if prev_y != None:
            prev_y.next = curr_x
        else:
            self.head = curr_x
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp
    
    def get_nth(self, index):
        current = self.head

        

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    # llist.print_list()
    llist.push(4)
    # llist.print_list()
    llist.insert_after(second, 5)
    llist.append(7)
    # llist.print_list()
    #llist.delete_node(1)
    #llist.print_list()
    llist.delete_node_position(4)
    llist.print_list()
    # print llist.get_count()
    # print llist.find_middle()
    # print llist.search(llist.head, 7)
    llist.swap_nodes(4, 2)
    llist.print_list()
        