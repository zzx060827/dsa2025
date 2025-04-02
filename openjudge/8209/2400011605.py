def MinFajo(budgets, m, Max, Min):
    def is_feasible(budgets, m, limit):
        sum = 0
        count = 1
        for i in range(len(budgets)):
            if budgets[i] > limit: return False
            if sum + budgets[i] <= limit:
                sum += budgets[i]
            else:
                count += 1
                sum = budgets[i]
        if count <= m: return True
        else: return False
    
    result = Max
    while Min <= Max:
        Mid = (Max + Min) // 2
        if is_feasible(budgets, m, Mid):
            result = min(result, Mid)
            Max = Mid - 1
        else:
            Min = Mid + 1

    return result

n, m = map(int, input().split())
budgets = []
for _ in range(n):
    budgets.append(int(input()))
print(MinFajo(budgets, m, sum(budgets), min(budgets)))