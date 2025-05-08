n = int(input())
ap = list(map(int, input().split()))
ap.sort(reverse = True)
ans = 0
while len(ap) > 1:
    last = ap[-1]
    for i in range(-2, -len(ap)-1, -1):
        if last > ap[i]:
            ap[i+1] = ap[i]
        else:
            ap[i+1] = last
            break;
    else:
        ap[0] = last
    ap[-2] += ap[-1]
    ap.pop()
    ans += ap[-1]
print(ans)
