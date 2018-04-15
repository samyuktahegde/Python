class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
            
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def min_value_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete_node(root, data):
    if root is None:
        return root
    if data<root.data:
        root.left = delete_node(root.left, data)
    elif data>root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root
            
        


r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

inorder(r)

delete_node(r, 30)
inorder(r)