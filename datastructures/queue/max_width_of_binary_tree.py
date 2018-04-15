class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_max_width(root):
    if root is None:
        return 0
    q = []
    max_width = 0
    q.insert(0, root)

    while (q!= []):
        count = len(q)
        print(count)
        max_width = max(max_width, count)
        while (count is not 0):
            count = count-1
            temp = q[0]
            q.pop()
            if temp.left is not None:
                q.insert(0, temp.left)
            if temp.right is not None:
                q.insert(0, temp.right)
    return max_width

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7) 
print(get_max_width(root))
