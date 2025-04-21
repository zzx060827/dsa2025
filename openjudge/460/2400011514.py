def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

import sys

for line in sys.stdin:
    strings = line.strip().split()
    if len(strings) != 2:
        continue  # 处理可能的意外输入
    X, Y = strings[0], strings[1]
    print(longest_common_subsequence(X, Y))