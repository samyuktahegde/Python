class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def are_mirror(rootA, rootB):
    if rootA is None and rootB is None:
        return True
    if rootA is None or rootB is None:
        return False
    return rootA.val==rootB.val and are_mirror(rootA.left, rootB.right) and are_mirror(rootA.right, rootB.left)

rootA = Node(1)
rootA.left = Node(3)
rootA.right = Node(2)
rootA.right.left = Node(5)
rootA.right.right = Node(4)

rootB = Node(1)
rootB.left = Node(2)
rootB.right = Node(3)
rootB.left.left = Node(4)
rootB.left.right = Node(5)

print(are_mirror(rootA, rootB))