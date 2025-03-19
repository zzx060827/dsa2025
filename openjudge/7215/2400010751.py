def integer_partitions(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(n + 1):
        dp[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j:
                dp[i][j] = dp[i][i]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]

    return dp[n][n]

#感觉和分盘子有点像
def num_of_plates(n,m):
    if n==0:
        return 1
    elif m==1:
        return 1
    else:
        if n-m>=0:
            return num_of_plates(n-m,m)+num_of_plates(n,m-1)

        else:
            return num_of_plates(n,n)
while True:
    try:
        n = int(input())
        if 0 < n <= 50:
            print(num_of_plates(n,n))
    except EOFError:
        break