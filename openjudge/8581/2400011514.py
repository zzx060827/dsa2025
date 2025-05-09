class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder):
    if not preorder:
        return None
    val = preorder.pop(0)
    if val == '.':
        return None
    node = TreeNode(val)
    node.left = build_tree(preorder)
    node.right = build_tree(preorder)
    return node

def inorder_traversal(root):
    if not root:
        return ''
    left = inorder_traversal(root.left)
    right = inorder_traversal(root.right)
    return left + root.val + right

def postorder_traversal(root):
    if not root:
        return ''
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    return left + right + root.val

# 读取输入
preorder_sequence = list(input().strip())

# 构建二叉树
root = build_tree(preorder_sequence)

# 获取中序和后序序列
inorder = inorder_traversal(root)
postorder = postorder_traversal(root)

# 输出结果
print(inorder)
print(postorder)