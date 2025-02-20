import timeit

def paths(row, col, M, N):
    if row==M or col==N : return 1
    return paths(row+1, col, M, N) \
         + paths(row, col+1, M, N)

def pathsDP(M, N):
    paths = [[0]*N+[1] for _ in range(M)]
    paths += [[1]*N]
    for j in range(M-1, -1, -1):
        for i in range(N-1, -1, -1):
            paths[j][i] = paths[j+1][i] \
                    + paths[j][i+1]
    return paths[0][0]

if __name__ == "__main__":
    print(paths(0, 0, 4, 5))
    print(pathsDP(100, 100))
    #print(timeit.timeit("paths(0, 0, 10000, 10000)", "from __main__ import paths"))
    #print(timeit.timeit("pathsDP(100, 100)", "from __main__ import pathsDP"))
