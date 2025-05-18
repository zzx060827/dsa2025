import heapq

n = int(input())
lengths = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    heapq.heapify(lengths)
    total_cost = 0
    
    while len(lengths) > 1:
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)
        cost = a + b
        total_cost += cost
        heapq.heappush(lengths, cost)
    
    print(total_cost)