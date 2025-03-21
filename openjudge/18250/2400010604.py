def find(x, parent):
    """查找x的根节点，并进行路径压缩"""
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    """合并x和y所在的集合"""
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_y] = root_x

def solve():
    while True:
        try:
            n, m = map(int, input().split())
        except EOFError:
            break

        # 初始化并查集
        parent = list(range(n + 1))  # 0到n的编号

        # 处理m次操作
        for _ in range(m):
            x, y = map(int, input().split())
            root_x = find(x, parent)
            root_y = find(y, parent)
            if root_x == root_y:
                print("Yes")
            else:
                union(x, y, parent)
                print("No")

        # 统计结果
        root_set = set()
        for i in range(1, n + 1):
            root_set.add(find(i, parent))

        # 输出结果
        print(len(root_set))
        print(" ".join(map(str, sorted(root_set))))

if __name__ == "__main__":
    solve()