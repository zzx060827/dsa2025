from collections import deque


def dfs(matrix, i, j, island_num): #找到2个孤岛
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != '1':
        return
    matrix[i][j] = island_num
    dfs(matrix, i + 1, j, island_num)
    dfs(matrix, i - 1, j, island_num)
    dfs(matrix, i, j + 1, island_num)
    dfs(matrix, i, j - 1, island_num)


def bfs(matrix, island_num): #找到2个岛最短
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == island_num:
                queue.append((i, j, 0))
    while queue:
        x, y, steps = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if matrix[new_x][new_y] == -island_num:
                    return steps
                elif matrix[new_x][new_y] == '0':
                    matrix[new_x][new_y] = island_num
                    queue.append((new_x, new_y, steps + 1))


n = int(input())
matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)
# 标记两个孤岛
island_count = 2
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '1':
            dfs(matrix, i, j, island_count)
            island_count = -2
# 从一个孤岛开始BFS找另一个孤岛
result = bfs(matrix, 2)
print(result)