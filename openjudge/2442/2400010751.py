from collections import Counter
def four_sum_zero(n, arrays):
    A, B, C, D = zip(*arrays)
    AB_map = Counter(a + b for a in A for b in B)
    count = sum(AB_map[-(c + d)] for c in C for d in D if -(c + d) in AB_map)
    return count
n = int(input())
arrays = [tuple(map(int, input().split())) for _ in range(n)]
print(four_sum_zero(n, arrays))
