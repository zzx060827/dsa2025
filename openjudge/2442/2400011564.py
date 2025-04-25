# 按照要求读入数据。
n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a);B.append(b);C.append(c);D.append(d)
# 建立记录了A、B中所有元素组合的和的字典（哈希表）。
absum = {}
for i in A:
    for j in B:
        absum[i + j] = absum.get(i + j, 0) + 1
# 遍历C和D的所有元素组合，计算他们的和，在字典中查找该和的相反数出现次数。
cnt = 0
for i in C:
    for j in D:
        cnt += absum.get(-(i + j), 0)
# 输出结果。
print(cnt)
