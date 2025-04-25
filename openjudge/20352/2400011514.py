n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s2 == 0 or len_s1 < len_s2:
        print("no")
        continue
    positions = []
    start = 0
    while start <= len_s1 - len_s2:
        pos = s1.find(s2, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + len_s2
    if not positions:
        print("no")
    else:
        print(' '.join(map(str, positions)) + ' ')