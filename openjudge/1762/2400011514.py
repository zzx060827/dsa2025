n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

dp = [0] * n
dp[0] = triangle[0][0]

for i in range(1, n):
    for j in range(i, -1, -1):
        current = triangle[i][j]
        if j == 0:
            dp[j] += current
        elif j == i:
            dp[j] = dp[j-1] + current
        else:
            dp[j] = max(dp[j-1], dp[j]) + current

print(max(dp))