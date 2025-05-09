dp = [0] * (31)
dp[0] = 1
for i in range(2,31,2):
    dp[i] = 3 * dp[i - 2] + sum(2*dp[i - 2*j] for j in range(2,16) if i - 2 * j >= 0)
    # 两列的排法有3种，所以有3*dp[i-2]这一项，后面的项是因为最后的2*j行可以是像是题干图片中最后四列的结构，或者它的上下翻转。
    # 由于输入保证n不超过30，所以我们可以预先处理出答案列表，这样可以显著减少计算量。
while True:
    n = int(input())
    if n == -1:
        exit(0)
    print(dp[n])
