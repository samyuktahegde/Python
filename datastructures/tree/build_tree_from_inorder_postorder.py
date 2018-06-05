class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(in_order, post_order)


def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.data, end= " ")
    print_in_order(node.right)