broad = [(0, None), (1, None), (2, None), (3, None), (4, None), (5, None), (6, None), (7, None)] # 初始化棋盘
cnt = 1 # 记录现在在产生第几种解法
# oj似乎在处理global的时候会有问题，如果不把global的变量放在函数前面，就会编译错误：
# E0602: Undefined variable 'cnt' (undefined-variable)
def placeQueen(num):
    """
    放皇后并且检查这个子儿是否合法。
    :param num: 已经放了的皇后个数，或者说，由于我们知道每一列只能有一个皇后，这也可以理解为在第几列进行讨论。
    :return: None
    """
    global cnt
    global broad
    if num == 8: # 如果已经放了8个皇后
        output()
        cnt += 1 # 记录的解法数加一
    for i in range(8): # 遍历每一行
        still_ok = True
        for j in range(num): # 检查现在操作的棋子之前放下的每一个棋子与现在操作棋子的位置关系，从而判断放置是否合规。
            if broad[j][1] == i or num - j == abs(broad[j][1] - i): # 在同一行或者在对角线上（不可能在同一列，参见num参数说明）
                still_ok = False
        if still_ok: # 通过检查的话
            broad[num] = (num, i) # 在刚刚讨论过了的位置放下一个棋子。
            placeQueen(num + 1) # 讨论下一列
            broad[num] = (num, None) # 回溯情况，相应列的棋子清空。

def output():
    """
    按照要求输出棋盘
    :return:None
    """
    print(f'No. {cnt}') # 输出解法的序号
    square_broad = [['0'] * 8 for i in range(8)] # 按照要求输出棋盘
    for i in broad:
        square_broad[i[1]][i[0]] = '1' # 有棋子的地方是1
    for i in square_broad:
        print(*i)

placeQueen(0)
