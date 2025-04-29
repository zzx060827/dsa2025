class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)
nums = list(map(int, input().split()))
root = None
for num in nums:
    root = insert(root, num)
result = []
preorder(root, result)
print(' '.join(map(str, result)))
################################################
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root
def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)
def main():
    input_line = input().strip()
    numbers = list(map(int, input_line.split()))
    root = None
    for number in numbers:
        root = insert(root, number)
    result = preorder_traversal(root)
    print(' '.join(map(str, result)))
if __name__ == '__main__':
    main()
"""