n, k = map(int, input().split())
num_str = input().strip()

# 预处理num[l..r]（1-based）
num = [[0] * (n + 1) for _ in range(n + 1)]
for l in range(1, n + 1):
    for r in range(l, n + 1):
        num[l][r] = int(num_str[l-1:r])

# 初始化dp表
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = num[1][i]

# 动态规划
for j in range(1, k + 1):
    for i in range(j + 1, n + 1):
        for m in range(j, i):
            dp[i][j] = max(dp[i][j], dp[m][j - 1] * num[m + 1][i])

print(dp[n][k])