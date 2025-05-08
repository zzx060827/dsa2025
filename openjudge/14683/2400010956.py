n = int(input())
ap = list(map(int, input().split()))
ap.sort(reverse = True)
ans = 0
while len(ap) > 1:
    i = -2
    while i >= -len(ap) and ap[-1] > ap[i]:
        i -= 1
    ap[-1], ap[i + 1] = ap[i + 1], ap[-1]
    ap[-2] += ap[-1]
    ap.pop()
    ans += ap[-1]
print(ans)
