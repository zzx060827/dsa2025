n, c = map(int, input().split())
stalls = sorted(int(input()) for _ in range(n))

low, high = 1, stalls[-1] - stalls[0]

def can_place_cows(distance):
    count, last_position = 1, stalls[0]
    for i in range(1, n):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count == c:
                return True
    return False

while low < high:
    mid = (low + high + 1) // 2
    if can_place_cows(mid):
        low = mid
    else:
        high = mid - 1

print(low)
