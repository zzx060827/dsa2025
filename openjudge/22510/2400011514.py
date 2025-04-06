import sys
import heapq

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    M = int(next(it))
    
    # 顶点编号：0和1为特殊点，森林隘口编号为2..N+1
    # defeat_time[v] 仅对 v>=2 定义，其他点的战斗时间视为0
    defeat = [0] * (N + 2)
    for i in range(2, N+2):
        defeat[i] = int(next(it))
    
    # 构建图，采用邻接表表示，图的顶点范围为 0 .. N+1
    graph = [[] for _ in range(N+2)]
    
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        t = int(next(it))
        # u -> v
        cost_uv = t + (defeat[v] if v >= 2 else 0)
        graph[u].append((v, cost_uv))
        # v -> u
        cost_vu = t + (defeat[u] if u >= 2 else 0)
        graph[v].append((u, cost_vu))
    
    # Dijkstra算法求最短路，从起点0到终点1
    INF = float('inf')
    dist = [INF] * (N+2)
    dist[0] = 0
    heap = [(0, 0)]  # (当前距离, 顶点)
    
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        # 如果到达终点，则可以结束（因为图正权）
        if u == 1:
            break
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    
    # 输出答案
    print(dist[1])

if __name__ == '__main__':
    main()
