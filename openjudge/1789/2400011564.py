def count24(numl:list):
    if len(numl) == 1: # 如果列表长度为1，那么比较列表中唯一一个元素是否等于24
        if abs(numl[0] - 24) <= 0.0001:
            return True
        else:
            return False # 我们需要避免浮点误差对计算结果造成影响
    for i in range(len(numl) - 1): # 如果列表长度超过1，那么在列表中选择两个数字进行运算
        for j in range(i + 1, len(numl)):
            n1 = numl[i]
            n2 = numl[j]
            can = [n1 + n2, n1 - n2, n2 - n1, n1 * n2]
            if abs(n2 - 0) > 0.0001:
                can.append(n1 / n2)
            if abs(n1 - 0) > 0.0001:
                can.append(n2 / n1) # can列表中存储了这两个选定的数字可以进行的二元运算方式
            for v in can:
                newl = [v] # 构造一个新的列表，先放进计算结果
                for _ in range(len(numl)):
                    if _ != i and _ != j: # 然后放进刚刚没有被计算的数字
                        newl.append(numl[_])
                if count24(newl): # 递归来考虑这个长度少了一的列表能否算出24，如果能，那么这个也能
                    return True
    return False # 如果这个列表的所有方法都试过了没有一个能算出24，那返回不能算出24

while True:
    numl = list(map(int, input().split()))
    if numl == [0, 0, 0, 0]:
        exit(0) # 输入数据并且判断是否结束
    if count24(numl):
        print('YES')
    else:
        print('NO')
