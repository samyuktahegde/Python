class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def in_order(root):
    if root:
        in_order(root.left)
        print (root.val)
        in_order(root.right)

def pre_order(root):
    if root:
        print (root.val)
        pre_order(root.left)
        pre_order(root.right)        

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right) 
        print (root.val)

# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
pre_order(root)
 
print "\nInorder traversal of binary tree is"
in_order(root)
 
print "\nPostorder traversal of binary tree is"
post_order(root)
            
