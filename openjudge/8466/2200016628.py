# 每个数字所需火柴棍数量
nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def count_matches(num):
    if num == 0:
        return nums[0]
    count = 0
    while num > 0:
        count += nums[num % 10]
        num //= 10
    return count


n = int(input())
# 减去加号和等号占用的火柴棍数量
n -= 4
count = 0
for a in range(1000):
    for b in range(1000):
        c = a + b
        if count_matches(a) + count_matches(b) + count_matches(c) == n:
            count += 1
print(count)