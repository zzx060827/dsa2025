n = int(input())

if n == 0:
    print(0)
else:
    prev_prev, prev = 0, 1  # N(0)和N(1)
    max_h = 1  # 初始情况下，n>=1，所以至少h=1
    h = 2  # 从h=2开始计算
    while True:
        current = 1 + prev + prev_prev
        if current > n:
            break
        max_h = h
        prev_prev, prev = prev, current
        h += 1
    print(max_h)