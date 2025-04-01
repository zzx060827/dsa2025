numbers = list(map(int, input().split()))
odds = []
evens = []

for num in numbers:
    if num % 2 == 1:
        odds.append(num)
    else:
        evens.append(num)

# 奇数从大到小排序
odds.sort(reverse=True)
# 偶数从小到大排序
evens.sort()

result = odds + evens
print(' '.join(map(str, result)))