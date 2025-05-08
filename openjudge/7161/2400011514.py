from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(sequence):
    if not sequence:
        return None
    nodes = sequence.split()
    # 每两个元素为一个节点和度数对
    queue = deque()
    root = Node(nodes[0])
    queue.append((root, int(nodes[1])))
    index = 2
    while queue and index < len(nodes):
        current_node, degree = queue.popleft()
        for _ in range(degree):
            if index >= len(nodes):
                break
            child_value = nodes[index]
            child_degree = int(nodes[index + 1])
            child_node = Node(child_value)
            current_node.children.append(child_node)
            queue.append((child_node, child_degree))
            index += 2
    return root

def post_order_traversal(root, result):
    if not root:
        return
    for child in root.children:
        post_order_traversal(child, result)
    result.append(root.value)

n = int(input())
trees = []
for _ in range(n):
    seq = input().strip()
    trees.append(seq)

forest = []
for seq in trees:
    root = build_tree(seq)
    forest.append(root)

result = []
for tree in forest:
    post_order_traversal(tree, result)

print(' '.join(result))