class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_expression_tree(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if token.islower() :
            # 操作数：直接变成叶子节点
            node = TreeNode(token)
            stack.append(node)
        else:
            # 运算符：弹出两个子树
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

    # 返回根节点
    return stack[0] if stack else None

from collections import deque
def level_order(root):
    if not root:
        return ""
    result = ""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result += (node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result[::-1]

n =  int(input())
for _ in range(n):
    postfix_tokens = input()
    root = build_expression_tree(postfix_tokens)
    print(level_order(root))