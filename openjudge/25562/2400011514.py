import math

n = int(input())
result = math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))
print(result)