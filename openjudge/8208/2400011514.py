R = int(input())
N = int(input())
rects = []
sum_small = 0
for _ in range(N):
    L, T, W, H = map(int, input().split())
    R_rect = L + W
    rects.append((L, R_rect, H))
    sum_small += W * H

if sum_small == 0:
    print(R)
    exit()

threshold = (sum_small + 1) // 2

def compute_sum(k):
    total = 0
    for L, R_rect, H in rects:
        if k >= R_rect:
            total += (R_rect - L) * H
        elif k > L:
            total += (k - L) * H
    return total

low, high = 0, R
k_low = R
while low <= high:
    mid = (low + high) // 2
    s = compute_sum(mid)
    if s >= threshold:
        k_low = mid
        high = mid - 1
    else:
        low = mid + 1

sum_min = compute_sum(k_low)

low_k, high_k = k_low, R
k_high = k_low
while low_k <= high_k:
    mid = (low_k + high_k) // 2
    s = compute_sum(mid)
    if s == sum_min:
        k_high = mid
        low_k = mid + 1
    else:
        high_k = mid - 1

print(k_high)