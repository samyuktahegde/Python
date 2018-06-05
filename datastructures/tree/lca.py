class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# def find_path(root, path, k):
#     if root is None:
#         return False
#     path.append(root.key)

#     if root.key == k:
#         return True

#     if((root.left != None and find_path(root.left, path, k)) or (root.right != None and find_path(root.right, path, k))):
#         return True

#     path.pop()
#     return False

# def find_lca(root, n1, n2):
#     path1 = []
#     path2 = []
#     if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
#         return -1
#     i = 0
#     while(i<len(path1) and i<len(path2)):
#         if path1[i] != path2[i]:
#             break
#         i+=1
#     return path1[i-1]

def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.key == n1 or root.key == n2:
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root        
    return left_lca if left_lca is not None else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(find_lca(root, 4, 5).key)

    
