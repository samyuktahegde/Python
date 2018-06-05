class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def max_depth(node):
    if node is None:
        return 0
    else:
        l_depth = max_depth(node.left)
        r_depth = max_depth(node.right)
        if l_depth>r_depth:
            return l_depth+1
        else:
            return r_depth+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(max_depth(root))

