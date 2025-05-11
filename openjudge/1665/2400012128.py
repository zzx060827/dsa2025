import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 0:
        return 1
    elif n == 2:
        return 3
    else:
        return 4*(f(n-2)) - f(n-4)

while True:
    k = int(input().strip())
    if k == -1:
        exit(0)
    if k % 2 == 1:
        print(0)
    else:
        print(f(k))