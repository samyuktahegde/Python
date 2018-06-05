class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_util(root, level):
    if root is None:
        return True
    print(root.data, level)

    if root.left is None and root.right is None:
        if check.leaf_level == 0:
            check.leaf_level = level
            return True
        return level == check.leaf_level
    return (check_util(root.left, level+1) and check_util(root.right, level+1))

def check(root):
    level = 0
    check.leaf_level = 0
    return check_util(root, level)

root = Node(12)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.left.left = Node(1)
root.left.right.left = Node(2)

if(check(root)):
    print("Leaves are at the same level")
else:
    print("Leaves are not at the same level")


