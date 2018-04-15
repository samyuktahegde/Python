class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0
    
    q = []
    q.append(root)
    height = 0
    while(True):
        nodecount = len(q)
        if nodecount==0:
            return height
        height+=1
        while (nodecount>0):
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            nodecount-=1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(tree_height(root))