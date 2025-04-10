def route(maze, k):
    m, n = len(maze), len(maze[0])
    visited = [ [[0] * k for _ in range(n)] for _ in range(m)]
    time = 0
    l1, l2 = [(i, j) for i in range(m) for j in range(n) if maze[i][j] == 'S'], []
    for i, j in l1:
        visited[i][j][0] = 1

    def nbr(i, j):
        for ii, jj in ((-1,0),(1,0),(0,-1),(0,1)):
            if i+ii in range(m) and j+jj in range(n):
                yield (i+ii, j+jj)

    while len(l1) > 0:
        time += 1
        for i, j in l1:
            for x, y in nbr(i, j):
                if visited[x][y][time % k] == 1:
                    continue
                if maze[x][y] in '.S' :
                    visited[x][y][time % k] = 1
                    l2.append((x, y))
                elif maze[x][y] == 'E' :
                    return time
                elif maze[x][y] == '#' and time % k == 0:
                    visited[x][y][0] = 1
                    l2.append((x, y))
        l1, l2 = l2, []
    else:
        return None

if __name__ == "__main__":
    for _ in range(int(input())):
        m, n, k = map(int, input().split())
        maze = [ list(input())[:n] for _ in range(m)]
        res = route(maze, k)
        print(res if res else "Oop!")

