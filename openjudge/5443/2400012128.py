import sys

def main():
    # 读取地点
    p = int(sys.stdin.readline())
    places = [sys.stdin.readline().strip() for _ in range(p)]
    place_to_idx = {place: i for i, place in enumerate(places)}
    
    # 初始化距离矩阵和路径矩阵
    INF = float('inf')
    dist = [[INF] * p for _ in range(p)]
    next_node = [[None] * p for _ in range(p)]
    
    for i in range(p):
        dist[i][i] = 0
        next_node[i][i] = i
    
    # 读取边信息
    q = int(sys.stdin.readline())
    for _ in range(q):
        u_str, v_str, d = sys.stdin.readline().split()
        d = int(d)
        u = place_to_idx[u_str]
        v = place_to_idx[v_str]
        if d < dist[u][v]:
            dist[u][v] = d
            dist[v][u] = d  # 无向图
            next_node[u][v] = v
            next_node[v][u] = u
    
    # Floyd-Warshall算法
    for k in range(p):
        for i in range(p):
            for j in range(p):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    
    # 处理查询
    r = int(sys.stdin.readline())
    for _ in range(r):
        start_str, end_str = sys.stdin.readline().split()
        start = place_to_idx[start_str]
        end = place_to_idx[end_str]
        
        # 构建路径
        if next_node[start][end] is None:
            print("No path")  # 根据样例，题目保证有解
        else:
            path = []
            at = start
            while at != end:
                path.append(at)
                at = next_node[at][end]
            path.append(end)
            
            # 输出结果
            result = [places[path[0]]]
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i+1]
                # 查找距离
                d = dist[u][v]
                result.append(f"->({d})->{places[v]}")
            print(''.join(result))

if __name__ == "__main__":
    main()    