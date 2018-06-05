class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(level_order, in_order):
    if in_order:
        for i in range(len(level_order)):
            if level_order[i] in in_order:
                node = Node(level_order[i])
                in_order_index = in_order.index(level_order[i])
                break
        if not in_order:
            return node
        node.left = build_tree(level_order, in_order[0:in_order_index])
        node.right = build_tree(level_order, in_order[in_order_index+1:len(in_order)])
        return node


def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.data, end=" ")
    print_in_order(node.right)

level_order = [20, 8, 22, 4, 12, 10, 14]
in_order = [4, 8, 10, 12, 14, 20, 22]
root = build_tree(level_order, in_order)
print_in_order(root)

