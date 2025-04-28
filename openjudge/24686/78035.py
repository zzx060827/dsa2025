import math

if __name__ == "__main__":
    k, n = (int(i) for i in input().split())
    treeSize = lambda i:2**(k - int(math.log2(i)))-1 
    tree = [[0, 0] for _ in range(2**k)]
    for _ in range(n):
        l = [int(i) for i in input().split()]
        if l[0] == 1:
            x, y = l[1:]
            tree[x][0] += y
            treeWeight = y * treeSize(x)
            "子树重量对其根结点和祖先结点的重量贡献"
            while x>=1:      
                tree[x][1] += treeWeight
                x //= 2
        elif l[0] == 2:
            x = l[1]
            weight = tree[x][1]
            z = x // 2      
            "祖先结点对子树的重量贡献"
            ts = treeSize(x)
            while z>=1:
                weight += tree[z][0] * ts
                z //= 2
            print(weight)

