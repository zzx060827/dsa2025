import math
#solution1
def max_income_maxk(prices):#时间复杂度O（n）
    n = len(prices)
    f = [[[None for i in range(n)]for p in range(3)]for j in range(2)]#记忆化搜索
    def dfs(i,j,hold):#i表示还剩i天，j表示仍可进行的交易次数，hold表示是否持有股票，1表示持有 0表示不持有
        if j < 0:
            return -math.inf
        elif i < 0 :
            return -math.inf if hold else 0
        if f[hold][j][i] != None:
            return f[hold][j][i]
        if hold:
            f[hold][j][i] = max(dfs(i-1,j,1),dfs(i-1,j-1,0)-prices[i])#注意是买入今天的股票
            return f[hold][j][i]
        else:
            f[hold][j][i] = max(dfs(i-1,j,0),dfs(i-1,j,1)+prices[i])#卖出股票#增加一次交易次数
            return f[hold][j][i]
    return dfs(n-1,2,0)
ans = []
n = int(input())
for i in range(n):
    m = int(input())
    prices = list(map(int,input().split()))
    ans.append(max_income_maxk(prices))
for i in ans:
    print(i)

#solution2
def maxProfit(prices):
    n = len(prices)
    if n == 0:
        return 0

    left_profit = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)

    right_profit = [0] * n
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profit[i] = max(right_profit[i + 1], max_price - prices[i])

    max_total_profit = 0
    for i in range(n):
        max_total_profit = max(max_total_profit, left_profit[i] + right_profit[i])

    return max_total_profit

ans=[]
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    ans.append(maxProfit(prices))
for i in ans:
    print(i)
