import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def build_tree(lines):
    root = None
    stack = []  # Each element is (node, indent_level)
    
    for line in lines:
        stripped_line = line.lstrip('\t')
        indent_level = len(line) - len(stripped_line)
        node_val = stripped_line.strip()
        if not node_val:
            continue
        
        node = TreeNode(node_val)
        
        if indent_level == 0:
            root = node
            stack = [(node, 0)]
        else:
            while stack and stack[-1][1] >= indent_level:
                stack.pop()
            parent, _ = stack[-1]
            parent.children.append(node)
            stack.append((node, indent_level))
    
    return root

def preorder(root):
    if not root:
        return []
    result = [root.val]
    for child in root.children:
        result.extend(preorder(child))
    return result

def postorder(root):
    if not root:
        return []
    result = []
    for child in root.children:
        result.extend(postorder(child))
    result.append(root.val)
    return result

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    
    root = build_tree(lines)
    
    pre = preorder(root)
    post = postorder(root)
    
    print(''.join(pre))
    print(''.join(post))

if __name__ == '__main__':
    main()