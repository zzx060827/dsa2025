def defs_ordinary_tree(arr):
    count = 0
    ans = 0
    for i in arr:
        if i == "d":
            count += 1
            ans = max(ans,count)
        else:
            count -= 1
    return ans
class binary_tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def build(arr):
    stack = []
    root = binary_tree(1)
    stack.append(root)
    for i in arr:
        if i == "d":
            node = binary_tree(1)
            if not stack[-1].left:
                stack[-1].left = node
            else:
                cur = stack[-1].left
                while cur.right:
                    cur = cur.right
                cur.right = node
            stack.append(node)
        else:
            stack.pop()
    return root
def dfs_binary_tree(root):
    if not root:
        return 0
    left = dfs_binary_tree(root.left)
    right = dfs_binary_tree(root.right)
    return max(left,right) + 1
s = input().strip()
a = defs_ordinary_tree(s)
root = build(s)
b = dfs_binary_tree(root)
print(f"{a} => {b-1}")        