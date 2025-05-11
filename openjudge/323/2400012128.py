while True:
    n,k = map(int,input().strip().split())
    if n == -1 and k == -1:
        break
    def check(board,x,y,jie):
        if board[x][y] == 1 or board[x][y] == ".":
            return False
        for i in range(y,-1,-1):
            if board[x][i] == 1:
                return False
        return True
    
    count = 0
    def solve(board,col,queen,jie):
        global count
        if queen == 0:
            count += 1
            return
        if queen + col > jie:
            return
        for i in range(jie):
            if check(board,i,col,jie):
                board[i][col] = 1
                solve(board,col+1,queen-1,jie)
                board[i][col] = 0
        solve(board,col+1,queen,jie)
    board = [["."]*n for _ in range(n)]
    for i in range(n):
        h = input().strip()
        for j in range(n):
            if h[j] == "#":
                board[i][j] = 0
    solve(board,0,k,n)
    print(count)