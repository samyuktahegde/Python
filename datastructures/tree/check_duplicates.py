class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def check_duplicate(root, hash_set):
    # print(hash_set)
    if root==None:
        return False
    if root.val in hash_set:
        return True
    hash_set.add(root.val)
    return check_duplicate(root.left, hash_set) or check_duplicate(root.right, hash_set)

root = Node(10)
root.left = Node(20)
root.right = Node(10)
# root.left.left = Node(20)
hash_set = set()
print(check_duplicate(root, hash_set))

