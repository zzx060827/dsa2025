import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
    
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    in_queue = [False] * (n + 1)
    queue = deque([1])
    in_queue[1] = True
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    
    print(dist[n])

if __name__ == "__main__":
    main()