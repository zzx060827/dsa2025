# 使用环形队列实现
t = int(input())
for times in range(t):
    dq = [None] * 1001 # 建立一个足够大的列表，因为n <= 1000。
    head = 0
    rear = 0
    # 操作
    n = int(input())
    for activity in range(n):
        tYpe, x = map(int, input().split())
        if tYpe == 1:# 进队
            dq[rear] = x
            rear = (rear + 1) % 1001
        else:#pop
            if x == 0:# 队头出队
                head = (head + 1) % 1001
            else:# 队尾出队
                rear = (rear - 1) % 1001
    # 输出
    if head == rear:# 为空
        print('NULL')
    else:# 非空
        if head < rear:
            print(*dq[head:rear])
        else:
            cache = dq[head:] + dq[:rear]
            print(*cache)
