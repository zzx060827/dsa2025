def herb(T, M, herbs):
    dp =[[0]*(T + 1) for i in range(M + 1)]
    for i in range(1, M + 1):
        time, value = herbs[i - 1]
        for j in range(T + 1):
            # 不采
            dp[i][j] = dp[i - 1][j]
            # 采
            if j >= time:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - time] + value)
    return dp[M][T]

T, M = map(int, input().split())  # 总时间，草药数量
herbs=[]
for _ in range(M):
    time,value=map(int,input().split())
    herbs.append((time,value))

print(herb(T, M, herbs))