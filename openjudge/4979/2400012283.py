n=int(input())
time=[]
for _ in range(n):
    li=list(map(int,input().split()))
    time.append(li)

dp=[[float('inf')]*n for _ in range(1<<n)] #从0到x的时间

dp[1][0]=0 #0到0

for exp in range(1<<n): #全部都走过
    for i in range(n):
        if dp[exp][i]!=float('inf'): #0到i不是无穷
            for j in range(n):
                if not (exp & (1<<j)): #没去过j
                    newexp=exp|(1<<j) #保留去过的岛加j岛
                    dp[newexp][j]=min(dp[newexp][j],dp[exp][i]+time[i][j])
print(dp[(1<<n)-1][n-1]) #全去过，从起点