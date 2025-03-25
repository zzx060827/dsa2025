def factor(n): # 分解质因数，从小到大输出。
    ans = []
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        k = 1
        while k**2 < n:
            if n % k == 0:
                ans.append(k)
                ans.append(n // k)
            k += 1
        if k**2 == n:
            ans.append(k)
        return sorted(ans)

def trystick(leftsticks, leftlenth, start):
    """
    递归判断某一个数值能不能作为木棒的原长。
    :param leftsticks: 还需要拼出来的原长木棒的个数；
    :param leftlenth: 要拼完当前这个原长木棒所剩余的长度；
    :param start: 从第几号木棍开始尝试（因为木棒按照长度从大到小排列）；
    :return: 数值能不能作为原长。
    """
    global used # 引入全局变量来表明哪些木棒已经用过了
    if leftlenth < 0: # 剩余长度为负，说明拼不出来。
        return False
    if leftsticks == 0: # 剩余要拼出的原长木棒为0个，说明拼好了，拼得出来。
        return True
    if leftlenth == 0: # 当前这根木棒剩余长度为零，说明这个木棒拼好了，开始拼下一根。
        return trystick(leftsticks - 1, i, 0) # 剩余要拼出的木棒数量减少1，剩余长度恢复正在尝试的原长，开始的位置恢复为0。
    prev = 0 # 这个变量用来标记前一个试到的木棒的长度。
    for j in range(start, n):
        if not used[j] and sticks[j] != prev: # 如果木棒没有被用过而且长度和上一次试的不一样才试拼。
            used[j] = True # 把这个木棒改成用过了。
            if trystick(leftsticks, leftlenth - sticks[j], j + 1):
                # 拼上这个木棒之后，情况变成要拼出原厂木棒个数不变，剩余长度减少这个木棒的长度，从这个木棒的下一个开始试。
                return True # 拼上这个木棒之后拼得出来说明拼得出来。
            used[j] = False # 如果拼不出来那需要回溯到拼上之前的状态，把这个木棒改回没用过。
            prev = sticks[j] # 更新上一次尝试的木棒的长度。

while True:
    n = int(input())
    if n == 0: # 退出程序
        exit(0)
    sticks = list(map(int,input().split()))
    sticks.sort(reverse= True) # 从大到小排序以减少尝试的次数。
    total = sum(sticks)
    can = factor(total) # 可能的答案肯定的是所有木棒的长度之和的一个因子。
    for i in can:
        if i >= sticks[0]+sticks[-1]: # 答案肯定要大于等于最长的一根和最短的一根拼起来的长度。
            num = total // i # 要拼出的原长木棒的数量
            used = [False] * n # 全局变量标志某一个木棒是不是已经用过。
            if trystick(num, i, 0):
                print(i)
                break # 输出最小的一个之后跳出循环。
