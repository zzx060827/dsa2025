n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

numbers.sort()
left = 0
right = n - 1
found = False

while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
        print(numbers[left], numbers[right])
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No")