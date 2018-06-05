class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def build_tree(in_order, pre_order, in_start, in_end):
    if (in_start > in_end):
        return

    t_node = Node(pre_order[build_tree.pre_index])
    build_tree.pre_index+=1

    if in_start==in_end:
        return t_node

    in_index = search(in_order, in_start, in_end, t_node.data)
    t_node.left = build_tree(in_order, pre_order, in_start, in_index-1)
    t_node.right = build_tree(in_order, pre_order, in_index+1, in_end)

    return t_node

def search(array, start, end, value):
    for i in range(start, end+1):
        if array[i] == value:
            return i

def print_in_order(node):
    if node is None:
        return
    
    print_in_order(node.left)    
    print node.data,
    print_in_order(node.right)

inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
build_tree.pre_index = 0
root = build_tree(inOrder, preOrder, 0, len(inOrder)-1)
 
# Let us test the build tree by priting Inorder traversal
print "Inorder traversal of the constructed tree is"
print_in_order(root)
    

