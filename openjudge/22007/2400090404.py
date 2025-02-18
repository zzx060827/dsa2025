m = int(input())
def solveNQueens(n):
    ans = []
    col = [0]*n#用于记录皇后放置的列
    chess = [[] for i in range(n)]
    def valid(r,c):#判断斜对角皇后能否吃掉彼此
        for R in range(r):
            C = col[R]
            if r+c == R+C or r-c == R-C:
                return False
        return True

    def dfs(r,s):#r当前枚举的行号 s剩余可以枚举的列号
        if r==n:
            ans.append([f"{c}" for c in col])
            return
        for c in s:
            if valid(r,c):
                col[r] = c
                dfs(r+1,s-{c})
    dfs(0,set(range(n)))
    cnt = 1
    if ans:
        for i in ans:
            print(' '.join(i)+' ')
    else:
        print('NO ANSWER')
solveNQueens(m)