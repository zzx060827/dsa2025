class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def parse_tree(s):
    if s == '*':
        return None
    if '(' not in s:
        return TreeNode(s)
    # 找到根节点和子树部分
    root_val = s[0]
    root = TreeNode(root_val)
    # 提取括号内的内容
    content = s.split('(', 1)[1].rstrip(')')
    # 分割左右子树
    balance = 0
    split_pos = -1
    for i, char in enumerate(content):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        elif char == ',' and balance == 0:
            split_pos = i
            break
    if split_pos == -1:
        # 只有左子树的情况
        left_str = content
        right_str = '*'
    else:
        left_str = content[:split_pos]
        right_str = content[split_pos+1:]
    root.left = parse_tree(left_str)
    root.right = parse_tree(right_str)
    return root

def preorder(root):
    if not root:
        return ''
    return root.val + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return ''
    return inorder(root.left) + root.val + inorder(root.right)

n = int(input())
for _ in range(n):
    s = input().strip()
    root = parse_tree(s)
    pre = preorder(root)
    ino = inorder(root)
    print(pre)
    print(ino)