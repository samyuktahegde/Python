class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_full_tree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (is_full_tree(root.left) and is_full_tree(root.right))
    return False

root = Node(10)
root.left = Node(20)
root.right = Node(30)
 
root.left.right = Node(40)
root.left.left = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
 
root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.right.left = Node(80)
root.left.right.right = Node(90)
root.right.left.left = Node(80)
root.right.left.right = Node(90)
root.right.right.left = Node(80)
# root.right.right.right = Node(90)

print(is_full_tree(root))