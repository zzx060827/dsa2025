def isok(i, num): # 判断是否为符合要求的位置
    for col in range(i):
        if res[col] == num or abs(res[col] - num) == abs(i - col):
            return False
    return True

def putq(col):
    global res, ans
    if col == N: # 如果列数为N，说明已经摆好一个完整的棋盘，输出到ans表中暂存。
        ans.append([res[_] for _ in range(0,N)])
        return
    for row in range(0, N): # 枚举一列中的每一个位置
        if isok(col, row): # 如果这个位置对于它之前的棋子来说是和要求的摆放
            res[col] = row # 在这个位置放上一个棋子
            putq(col + 1) # 递归到下一列
            res[col] = -1 # 拿走这个棋子
    return

N = int(input())
res = [-1] * (N)
ans = []
putq(0)
if ans: # 如果ans表不为空，输出。否则，输出"NO ANSWER"。
    for _ in ans:
        print(*_)
else:
    print("NO ANSWER")
