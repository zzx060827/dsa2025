n = int(input())
for _ in range(n):
    expr = input().strip()
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            elif token == '/':
                res = a / b
            stack.append(res)
        else:
            stack.append(float(token))
    print("{0:.2f}".format(stack[0]))