def sier(num): # 递归解决画Sierpinski分型问题
    if num == 1: # 递归边界条件，阶数为一。
        return [' /\\', '/__\\']
    else:
        temp = sier(num - 1) # 使用阶数少一的问题的答案来获得当前问题的答案。
        spacesf = ' ' * 2**(num - 1)
        return [spacesf + temp[_] for _ in range(len(temp))] + [temp[_] + (len(temp) - 1 - _) * ' ' + temp[_] for _ in range(len(temp))]
        # 在每行插入所需要的位置插入所需要数量的空格。

while True:
    n = int(input())
    if n == 0:
        exit(0)
    print('\n'.join(sier(n))) # 打印输出。
    print() # 题目要求"Print an empty line after each test case"。
