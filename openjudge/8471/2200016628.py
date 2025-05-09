def min_cut(s):
    n = len(s)
    if n <= 1:
        return 0

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):  # 从后往前填表，确保 is_pal[i+1][j-1] 先被填好
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True

    #dp[i] 表示 s[0..i] 最少需要切割几次
    dp = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = min(dp[j] + 1 for j in range(i) if is_pal[j + 1][i])
    return dp[-1]

T = int(input())
for _ in range(T):
    s = input().strip()
    print(min_cut(s))
