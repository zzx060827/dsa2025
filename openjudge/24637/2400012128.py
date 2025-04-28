class treenode:
    def __init__(self,val,l=None,r=None):
        self.v = val
        self.l = l
        self.r = r

n = int(input().strip())
lst = list(map(int,input().strip().split()))
treenodes = [treenode(i) for i in lst]
for i in range(n):
    if 2*i+1 < n:
        treenodes[i].l = treenodes[2*i+1]
    if 2*i+2 < n:
        treenodes[i].r = treenodes[2*i+2]

def dfs(root):
    if root == None:
        return 0,0
    l1,l2 = dfs(root.l)
    r1,r2 = dfs(root.r)
    root1 = root.v + l2 + r2
    root2 = max(l1,l2) + max(r2,r1)
    return root1,root2
print(max(dfs(treenodes[0])))