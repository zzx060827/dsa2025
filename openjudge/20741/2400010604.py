import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    grid = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    
    # Find all islands using BFS
    islands = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                island = []
                while queue:
                    x, y = queue.popleft()
                    island.append((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                islands.append(island)
    
    # There should be exactly two islands
    island1 = islands[0]
    island2 = islands[1]
    
    min_distance = float('inf')
    for (x1, y1) in island1:
        for (x2, y2) in island2:
            distance = abs(x1 - x2) + abs(y1 - y2) - 1
            if distance < min_distance:
                min_distance = distance
    
    print(min_distance)

if __name__ == "__main__":
    main()