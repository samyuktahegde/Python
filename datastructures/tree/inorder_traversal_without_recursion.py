class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def in_order(root):
    current = root
    s = []
    done = 0
    while not done:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s)>0):
                current = s.pop()
                print(current.data)
                current = current.right
            else:
                done = 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
in_order(root)