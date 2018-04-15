class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Conversion:
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def convert_list_to_binary(self):
        q = []
        if self.head is None:
            self.root = None
            return

        self.root = BinaryTreeNode(self.head.data)
        
        q.append(self.root)

        self.head = self.head.next
        while(self.head):
            current_parent = q.pop(0)
            left_child = None
            right_child = None
            left_child = BinaryTreeNode(self.head.data)
            q.append(left_child)
            self.head = self.head.next
            if self.head:
                right_child = BinaryTreeNode(self.head.data)
                q.append(right_child)
                self.head = self.head.next
            current_parent.left = left_child
            current_parent.right = right_child

    def in_order_traversal(self, root):
        if(root):
            self.in_order_traversal(root.left)
            print (root.data)
            self.in_order_traversal(root.right)

conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)
 
conv.convert_list_to_binary()
 
print("Inorder Traversal of the contructed Binary Tree is:")
conv.in_order_traversal(conv.root)

    
