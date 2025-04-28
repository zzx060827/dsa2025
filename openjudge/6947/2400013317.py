class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # first child
        self.right = None  # next sibling

def build_tree(s):
    root = Node(0)
    stack = [root]
    current_val = 1
    for c in s:
        if c == 'd':
            new_node = Node(current_val)
            stack[-1].add_child(new_node)
            stack.append(new_node)
            current_val += 1
        elif c == 'u':
            stack.pop()
    return root

def tree_height(root):
    if not root.children:
        return 0
    max_height = 0
    for child in root.children:
        child_height = tree_height(child)
        if child_height > max_height:
            max_height = child_height
    return max_height + 1

def convert_to_binary(root):
    if not root:
        return None
    binary_root = BinaryNode(root.val)
    if root.children:
        binary_root.left = convert_to_binary(root.children[0])
        current = binary_root.left
        for child in root.children[1:]:
            current.right = convert_to_binary(child)
            current = current.right
    return binary_root

def binary_tree_height(root):
    if not root:
        return -1
    left_height = binary_tree_height(root.left)
    right_height = binary_tree_height(root.right)
    return max(left_height, right_height) + 1

s = input().strip()
original_tree = build_tree(s)
h1 = tree_height(original_tree)
binary_tree = convert_to_binary(original_tree)
h2 = binary_tree_height(binary_tree)
print(f"{h1} => {h2}")
