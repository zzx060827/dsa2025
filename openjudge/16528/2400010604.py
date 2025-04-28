n = int(input())
activities = []
for _ in range(n):
    s, e = map(int, input().split())
    activities.append((e, s))  # 存储为（结束时间，开始时间）便于排序

# 按结束时间升序排序
activities.sort()

count = 0
last_end = -1  # 初始化上一个活动的结束时间，确保第一个活动可以选

for e, s in activities:
    if s > last_end:
        count += 1
        last_end = e

print(count)