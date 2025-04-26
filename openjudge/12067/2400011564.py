def isvalid(num): # 确定是否是可能通过放弃k场考试得到的分数值
    v = []
    for i in range(len(a)):
        v.append(a[i] - num * b[i] / 100)
    v.sort(reverse=True)
    p = sum(v[:s])
    if p >= 0:
        return True
    else:
        return False


while True:
    # 读入数据
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        exit(0)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = n - k
    # 二分查找
    left = 0
    right = 100
    while right - left > 0.001:
        mid = (left + right) / 2
        if isvalid(mid):
            left = mid
        else:
            right = mid
    # 输出
    print(f'{left:.0f}')
