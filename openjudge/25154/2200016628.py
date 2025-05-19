class GeneralTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []  # 多个子节点


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None   # 指向第一个孩子
        self.right = None  # 指向下一个兄弟

def convert_to_binary_tree(node):
    if not node:
        return None
    b_node = BinaryTreeNode(node.val)
    if not node.children:
        return b_node

    # 第一个孩子作为 left
    b_node.left = convert_to_binary_tree(node.children[0])

    # 后续兄弟作为 right 链接
    current = b_node.left
    for child in node.children[1:]:
        current.right = convert_to_binary_tree(child)
        current = current.right
    return b_node

# 后序遍历（左-右-根）
def postorder(node):
    if not node:
        return ""
    return postorder(node.left) + postorder(node.right) + str(node.val)

# 构造普通树
nodes = {}  # 字母 -> GeneralTreeNode 映射

import sys
lines=[line for line in sys.stdin]
for line in  lines:
    parts = line.strip().split()
    parent_val = parts[0]
    if parent_val not in nodes:
        nodes[parent_val] = GeneralTreeNode(parent_val)
    parent = nodes[parent_val]

    for child_val in parts[1:]:
        if child_val not in nodes:
            nodes[child_val] = GeneralTreeNode(child_val)
        parent.children.append(nodes[child_val])

# 根节点就是第一行第一个字母
g_root = nodes[lines[0].split()[0]]

b_node=convert_to_binary_tree(g_root)
print(postorder(b_node))
