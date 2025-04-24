# 读取输入的成绩列表
scores = list(map(float, input().split()))
# 学生数量
n = len(scores)

# 二分查找的左右边界
left, right = 1, 1000000000

# 二分查找
while left < right:
    mid = (left + right) // 2
    # 计算当前的 a 值
    a = mid / 1000000000
    # 统计调分后成绩不小于 85 分的学生数量
    count = sum(1 for score in scores if score * a + 1.1 ** (score * a) >= 85)
    # 如果满足优秀人数比例不小于 60%，缩小右边界
    if count >= 0.6 * n:
        right = mid
    # 否则，缩小左边界
    else:
        left = mid + 1

# 输出结果
print(left)