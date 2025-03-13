N, M = map(int, input().split())
nums = list(map(int, input().split()))

bit_counts = [0] * 16
for num in nums:
    for i in range(16):
        if num & (1 << i):
            bit_counts[i] += 1

offset = 0
res = []

for _ in range(M):
    cmd, val = input().split()
    val = int(val)
    if cmd == 'C':
        offset = (offset + val) % 65536
    elif cmd == 'Q':
        cnt = 0
        mask = 1 << val
        for i in range(16):
            if (offset & (1 << i)):
                real_bit = (val - i + 16) % 16
                cnt += (N - bit_counts[real_bit]) if mask & (1 << i) else bit_counts[real_bit]
            else:
                real_bit = (val - i + 16) % 16
                cnt += bit_counts[real_bit] if mask & (1 << i) else 0
        res.append(cnt)

for ans in res:
    print(ans)
