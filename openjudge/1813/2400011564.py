lights = []
for _ in range(5):
    lights.append(list(map(int, input().split()))) # 读入数据
for t in range(64): # 对每一个第一行的情况进行枚举。
    ans = []
    s = bin(t)
    firstrow = [0] * (6 - (len(s) - 2)) + list(map(int, s[2:])) # 通过二进制，生成了64种情况。
    ans.append(firstrow)
    cache = [[lights[i][j] for j in range(6)] for i in range(5)] # 注意不能浅拷贝。
    if firstrow[0] == 1: # 处理第一排的数据。
        cache[0][0] ^= 1
        cache[0][1] ^= 1
        cache[1][0] ^= 1
    if firstrow[-1] == 1:
        cache[0][-1] ^= 1
        cache[0][-2] ^= 1
        cache[1][-1] ^= 1
    for j in range(1, 5):
        if firstrow[j] == 1:
            cache[0][j - 1] ^= 1
            cache[0][j] ^= 1
            cache[0][j + 1] ^= 1
            cache[1][j] ^= 1
    for row in range(1, 4): # 处理二三四排。
        thisrow = cache[row - 1]
        ans.append([thisrow[_] for _ in range(6)]) # 注意不能浅拷贝。
        if thisrow[0] == 1:
            cache[row][0] ^= 1
            cache[row][1] ^= 1
            cache[row - 1][0] ^= 1
            cache[row + 1][0] ^= 1
        if thisrow[-1] == 1:
            cache[row][-1] ^= 1
            cache[row][-2] ^= 1
            cache[row - 1][-1] ^= 1
            cache[row + 1][-1] ^= 1
        for j in range(1, 5):
            if thisrow[j] == 1:
                cache[row][j - 1] ^= 1
                cache[row][j] ^= 1
                cache[row][j + 1] ^= 1
                cache[row - 1][j] ^= 1
                cache[row + 1][j] ^= 1
    lastrow = cache[3]
    ans.append([lastrow[_] for _ in range(6)]) # 注意不能浅拷贝。
    if lastrow[0] == 1: # 处理最后一排
        cache[-1][0] ^= 1
        cache[-1][1] ^= 1
        cache[-2][0] ^= 1
    for j in range(1, 5):
        if lastrow[j] == 1:
            cache[-1][j - 1] ^= 1
            cache[-1][j] ^= 1
            cache[-1][j + 1] ^= 1
            cache[-2][j] ^= 1
    if lastrow[-1] == 1:
        cache[-1][-1] ^= 1
        cache[-1][-2] ^= 1
        cache[-2][-1] ^= 1
    if 1 not in cache[-1]: # 检查最后一排的灯是否全部熄灭了。
        for i in range(5):
            print(*ans[i]) # 按照格式要求输出。
        break
