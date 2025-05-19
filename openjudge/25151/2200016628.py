class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(s: str) -> TreeNode:
    def parse(index):
        if index >= len(s):
            return None, index

        # 空树
        if s[index] == '*':
            return None, index + 1

        # 读根节点
        root = TreeNode(s[index])
        index += 1

        if index < len(s) and s[index] == '(':
            index += 1
            # 先递归解析左子树
            left, index = parse(index)

            # 如果当前是逗号，说明还有右子树
            if index < len(s) and s[index] == ',':
                index += 1
                right, index = parse(index)
            else:
                right = None

            # 遇到 ')' 说明这个子树解析完毕
            if index < len(s) and s[index] == ')':
                index += 1

            root.left = left
            root.right = right

        return root, index

    tree, _ = parse(0)
    return tree


# 前序遍历（根-左-右）
def preorder(node):
    if not node:
        return ""
    return str(node.val) + preorder(node.left) + preorder(node.right)

# 中序遍历（左-根-右）
def inorder(node):
    if not node:
        return ""
    return inorder(node.left) + str(node.val) + inorder(node.right)

n = int(input())
for _ in range(n):
    s = input()
    root = build_tree(s)
    print(preorder(root))
    print(inorder(root))