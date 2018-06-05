class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_leaf_count(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return get_leaf_count(node.left)+get_leaf_count(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(get_leaf_count(root))