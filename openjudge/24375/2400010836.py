def factor(s): #求因数
    ans = set()
    for i in range(int(s ** 0.5) + 1):
        if not s % (i + 1):
            ans.add(i + 1)
            ans.add(s // (i + 1))
    return sorted(list(ans))

def check(lenth, l, pre): #检查拼法
    if not l and not pre: #完全拼完
        return True
    if not l and pre: # 冗余
        return False
    if lenth < pre + l[-1]: # 由于l降序排列，可以剪枝
        return False
    else:
        p = -1 #相同的木棍不用重复尝试，由于l有序，可以用p记录上一次check的木棍组合
        for i in range(len(l)):
            if l[i] == p: #避免重复尝试
                continue
            if l[i] > p:
                p = l[i]
            if pre + l[i] <= lenth:
                if check(lenth, l[:i:] + l[i + 1::], (pre + l[i]) % lenth):
                    return True #有可能的就返回True
            else:
                break
        return False

while True:
    n = int(input())
    if not n:
        break
    l = list(map(int, input().split()))
    l.sort(reverse=True) #降序排列，先考虑长度大的木棍，可能性少
    s = sum(l)
    f = factor(s)
    for i in f:
        if l[0] > i:
            continue
        if check(i, l, 0):
                print(i)
                break