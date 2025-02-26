def solve(n, times):
    dp = [[float('inf')]*n for _ in range(1 << n)]
    dp[1][0] = 0  #从1号岛屿开始对应mask=2**(1-1)=1

    for mask in range(1,1 << (n-1)):
        for i in range(n-1):  # 当前所在岛屿
            if mask & (1 << i):   # 如果当前岛屿i已被访问
                for j in range(1,n-1):  # 下一个要访问的岛屿
                    if not mask & (1 << j):  # 确保岛屿j尚未被访问
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + times[i][j])
    # 计算最终结果: 所有岛屿都已访问且最后一步是从某个岛屿到终点N
    final_mask = (1 << (n-1)) - 1  # 所有岛屿都已访问
    return min(dp[final_mask][i]+times[i][n-1] for i in range(n-1))  # 加上从最后一个岛屿到终点的时间

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, times))