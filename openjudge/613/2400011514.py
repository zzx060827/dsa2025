import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        
        parent = list(range(n))
        size = [1] * n
        
        def find(u):
            # 路径压缩的find函数
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # 路径压缩，直接指向祖父节点
                u = parent[u]
            return u
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return
            # 按秩合并
            if size[root_u] < size[root_v]:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
            else:
                parent[root_v] = root_u
                size[root_u] += size[root_v]
        
        for _ in range(m):
            parts = list(map(int, sys.stdin.readline().split()))
            k = parts[0]
            if k == 0:
                continue
            members = parts[1:]
            if k >= 2:
                first = members[0]
                for member in members[1:]:
                    union(first, member)
        
        # 查找0的根节点并输出对应的size
        root = find(0)
        print(size[root])

if __name__ == "__main__":
    main()