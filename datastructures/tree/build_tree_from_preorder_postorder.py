class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(pre_order, post_order):
    if post_order:
        