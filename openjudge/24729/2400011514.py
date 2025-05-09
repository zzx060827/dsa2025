def parse_tree(s):
    tree = {}
    stack = []
    current_node = None
    i = 0
    n = len(s)
    while i < n:
        if s[i].isupper():
            node = s[i]
            tree[node] = []
            if stack:
                parent = stack[-1]
                tree[parent].append(node)
            current_node = node
            i += 1
        elif s[i] == '(':
            stack.append(current_node)
            i += 1
        elif s[i] == ',':
            i += 1
        elif s[i] == ')':
            stack.pop()
            i += 1
    return tree

def preorder(tree, root):
    result = [root]
    for child in tree.get(root, []):
        result += preorder(tree, child)
    return result

def postorder(tree, root):
    result = []
    for child in tree.get(root, []):
        result += postorder(tree, child)
    result.append(root)
    return result

s = input().strip()
tree = parse_tree(s)
root = s[0]

pre = preorder(tree, root)
post = postorder(tree, root)

print(''.join(pre))
print(''.join(post))