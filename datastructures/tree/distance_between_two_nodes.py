class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def path_to_node(root, path, k):
    if root is None:
        return False
    path.append(root.data)
    if root.data == k:
        return True

    if((root.left != None and path_to_node(root.left, path, k)) or (root.right!=None and path_to_node(root.right, path, k))):
        return True

    path.pop()
    return False

def distance(root, data1, data2):
    if root:
        path1 = []
        path_to_node(root, path1, data1)

        path2 = []
        path_to_node(root, path2, data2)

        i = 0
        while i<len(path1) and i<len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1

        return len(path1)+len(path2)-2*i
    else:
        return 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

print(distance(root, 4, 5))

