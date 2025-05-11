from math import log

k, n = map(int, input().split())
tree1 = [0] * (1 << k)# 记录每个子树收到的操作
tree2 = [dict() for _ in range(1 << k)]# 记录每个子树操作对祖先产生的影响
numofnodes = [(1 << (k - int(log(x, 2)))) - 1 for x in range(1, 1 << k)]
for _ in range(n):
    action = list(map(int, input().split()))
    if action[0] == 1:
        tree1[action[1]] += action[2]
        i = 2
        r = action[1] // 2
        while r > 0:
            tree2[r].setdefault(i, 0)
            tree2[r][i] += action[2]
            r //= 2
            i *= 2
    else:
        r = action[1]
        s = 0
        while r > 0:
            s += tree1[r]
            r //= 2
        s *= numofnodes[action[1] - 1] # 计算祖树变动对该子树的影响
        for i in tree2[action[1]]:
            s += numofnodes[action[1] - 1] // i * tree2[action[1]][i]
        # 计算子辈树对该子树的影响
        print(s)
