clocks = []
for i in range(3):
    clocks.append(list(map(int, input().split()))) # 读入数据

can = [28]
for x1 in range(4):
    for x2 in range(4):
        for x3 in range(4): # 枚举前三个拨钟方法的情况。
            x4 = (4 - clocks[0][0] - x1 - x2) % 4
            x5 = (4 - clocks[0][1] - x1 - x2 - x3) % 4
            x6 = (4 - clocks[0][2] - x2 - x3) % 4
            x7 = (4 - clocks[1][0] - x1 - x4 - x5) % 4
            x8 = (4 - clocks[2][0] - x4 - x7) % 4
            x9 = (4 - clocks[1][1] - x1 - x3 - x5 - x7) % 4 # 推导出剩下六个播种方法的次数。
            if (x3 + x5 + x6 + x9) % 4 == (4 - clocks[1][2]) % 4\
                and (x5 + x7 + x8 + x9) % 4 == (4 - clocks[2][1]) % 4\
                and (x6 + x8 + x9) % 4 == (4 - clocks[2][2]) % 4: # 检验是否正确
                if sum((x1, x2, x3, x4, x5, x6, x7, x8, x9)) < sum(can):
                    can = [x1,x2,x3,x4,x5,x6,x7,x8,x9] # 如果正确，看它是不是比上一个正确情况更加简短的。
ans = ''
for i in range(9):
    ans += str(i + 1) * can[i]
print(*ans, sep=' ') # 按照要求输出。
