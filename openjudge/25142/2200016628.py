class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]

    left_postorder = postorder[:len(left_inorder)]
    right_postorder = postorder[len(left_inorder):-1]

    root.left = build_tree(left_inorder, left_postorder)
    root.right = build_tree(right_inorder, right_postorder)

    return root


def print_indented_tree(root):
    result = []

    def dfs(node, level):
        if not node:
            return

        # 当前节点行
        result.append('\t' * level + node.val)

        # 处理左子树
        if not node.left and node.right:
            # 左子树为空但右子树不空，添加'*'
            result.append('\t' * (level + 1) + '*')
        elif node.left:
            dfs(node.left, level + 1)

        # 处理右子树
        if node.right:
            dfs(node.right, level + 1)

    dfs(root, 0)
    return '\n'.join(result)

inorder=input()
postorder=input()
root=build_tree(inorder, postorder)
print(print_indented_tree(root))