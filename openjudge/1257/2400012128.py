def build(a,b):
    if not a or not b:
        return None
    root = a[0]
    index = b.index(root)
    left_b=b[:index]
    right_b=b[index+1:]
    left_a=a[1:1+index]
    right_a=a[1+index:]
    tl=build(left_a,left_b)
    tr=build(right_a,right_b)
    return root,tl,tr
def post(tree):
    if not tree:
        return ""
    return post(tree[1])+post(tree[2])+tree[0]
while True:    
    try:
        a,b=input().strip().split()
        tree=build(a,b)
        ans=post(tree)
        print(ans)
    except EOFError:
        break