class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeBuilder:
    def __init__(self, preorder):
        self.preorder = preorder
        self.index = 0  # 用来跟踪当前处理的位置

    def build_tree(self):
        if self.index >= len(self.preorder):
            return None
        ch = self.preorder[self.index]
        self.index += 1
        if ch == '.':
            return None
        node = TreeNode(ch)
        node.left = self.build_tree()
        node.right = self.build_tree()
        return node

def inorder(node):
    if not node:
        return ''
    return inorder(node.left) + node.val + inorder(node.right)

def postorder(node):
    if not node:
        return ''
    return postorder(node.left) + postorder(node.right) + node.val

preorder = input().strip()
builder = BinaryTreeBuilder(preorder)
root = builder.build_tree()

print(inorder(root))
print(postorder(root))
