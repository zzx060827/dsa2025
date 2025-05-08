def express(num): # 使用递归来解决
    temp = bin(num)[2:] # 通过转换为二进制来获得其2的幂次方表示
    digits = []
    for i in range(len(temp)):
        if temp[-i - 1] == '1':
            digits.append(i) # 准备需要进行进一步操作的数字
    res = []
    for i in reversed(digits): # 遍历每一个需要进一步转换的数字
        if i == 0: # 三个递归结束条件
            res.append('2(0)')
        elif i == 1:
            res.append('2')
        elif i == 2:
            res.append('2(2)')
        else:
            res.append(f'2({express(i)})') # 进行递归并且按照格式输出
    return '+'.join(res) # 拼接各个字符串

n = int(input())
print(express(n))
