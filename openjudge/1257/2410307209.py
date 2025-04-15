def build_postorder(preorder, inorder):
    if not preorder:
        return ""
    root = preorder[0]
    root_index = inorder.index(root)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[1+len(left_inorder):]
    return build_postorder(left_preorder, left_inorder) + build_postorder(right_preorder, right_inorder) + root

def main():
    import sys
    for line in sys.stdin:
        preorder, inorder = line.split()
        postorder = build_postorder(preorder, inorder)
        print(postorder)

if __name__ == "__main__":
    main()