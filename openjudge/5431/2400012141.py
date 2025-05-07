class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, val):
    if root is None:
        return TreeNode(val)
    '''
    按照二叉搜索树的定义，树中是不能有两个等值结点的，
    需要用后面的替换前面的，所以这里要判断三种情况：
       < , >, =
    从样例中可以看到这一点：输入两个827，但是只输出一个
    '''
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    else:
        pass
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
