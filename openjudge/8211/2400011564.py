def isvalid(v): # 判断是否是可能的体积
    cnt = sum(3.1415926536 * r**2 // v for r in pies) # 计算按照这个体积，可以分出来几份派。
    if cnt >= (f + 1): # 如果派的份数多于朋友数加一，则是可能的，否则是不可能的。
        return True
    else:
        return False

n, f = map(int,input().split())
pies = list(map(int,input().split())) # 输入数据。
left = 0
right = sum(3.1415926536 * r**2 for r in pies) / (f + 1)
# 进行二分搜索。其中初始上界可以设置为不考虑每个人的派“不能由几个派的小块拼成”时候每个人能分到的最大体积。
while right - left >= 0.00001: # 设置精确度要求。比输出所要求的位数多2位才可以。
    mid = (left + right) / 2
    if isvalid(mid):
        left = mid
    else:
        right = mid
print(f'{right:.3f}') # 输出结果。
