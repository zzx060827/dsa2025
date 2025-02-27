from collections import deque
def min_prize(n, m, matches):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in matches:
        graph[b].append(a)
        indegree[a] += 1
    prize = [100] * n
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        team = queue.popleft()
        for oppo in graph[team]:
            # 根据胜负关系调整奖金
            prize[oppo] = max(prize[oppo], prize[team] + 1)
            indegree[oppo]-=1
            if indegree[oppo]==0:
                queue.append(oppo)
    return sum(prize)
n,m=map(int,input().split())
matches=[tuple(map(int,input().split()))for _ in range(m)]
print(min_prize(n, m, matches))


#input().split()：获取每行输入并将其按空格分割成一个列表；
#map(int, ...)：将列表中的每个元素转成整数；
#tuple(...)：将转换后的结果转换成一个元组 (a, b)，表示队伍a打败了队伍b；
#[ ... for _ in range(m)]：将这种转换应用到m次输入。