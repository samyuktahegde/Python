class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view_util(root, level, max_level):
    if root is None:
        return
    if max_level[0]<level:
        print(root.data)
        max_level[0]=level
    left_view_util(root.left, level+1, max_level)
    left_view_util(root.right, level+1, max_level)

def left_view(root):
    max_level = [0]
    left_view_util(root, 1, max_level)

root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
 
left_view(root)