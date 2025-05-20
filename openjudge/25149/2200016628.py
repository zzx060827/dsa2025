class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_expression_tree(tokens):
    def helper(index):
        if index[0] >= len(tokens):
            return None

        token = tokens[index[0]]
        index[0] += 1

        node = TreeNode(token)

        if token.isupper():
            node.left = helper(index)
            node.right = helper(index)

        return node

    return helper([0])

# 层序遍历（按层逐层，从左到右）
from collections import deque
def level_order(root):
    if not root:
        return ""
    result = ""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result+=(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result[::-1]

n = int(input())
for _ in range(n):
    tokens = input()
    root = build_expression_tree(tokens)
    print(level_order(root))