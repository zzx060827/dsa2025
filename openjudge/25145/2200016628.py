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

from collections import deque
def level_order(root):
    if not root:
        return ""
    result = ""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result +=(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

n = int(input())
for _ in range(n):
    # 示例输入
    inorder = input()
    postorder = input()

    # 构建树并输出前序遍历
    root = build_tree(inorder, postorder)
    print(level_order(root))