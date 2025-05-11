#bfs找到最长的路
n,m=map(int,input().split())
adj=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
length=[0]*n
visited=[False]*n
def bfs(i):
    visited[i]=True
    if not adj[i]:
        length[i]=0
    else:
        for j in adj[i]:
            if not visited[j]:
                bfs(j)
            length[i]=max(length[i],length[j]+1)
for i in range(n):
    if not visited[i]:
        bfs(i)
print(sum(length)+100*n)



