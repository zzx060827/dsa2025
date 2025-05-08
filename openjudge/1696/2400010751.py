def evaluate(tokens):
    """
    递归解析波兰表达式并计算其值。
    :param tokens: 表达式拆分后的列表
    :return: 计算结果
    """
    token = tokens.pop(0)
    if token in {"+", "-", "*", "/"}:
        left = evaluate(tokens)
        right = evaluate(tokens)
        if token == "+":
            return left + right
        elif token == "-":
            return left - right
        elif token == "*":
            return left * right
        elif token == "/":
            return left / right
    else:
        return float(token)

input_line = input().strip()
tokens = input_line.split()
result = evaluate(tokens)
print(f"{result:.6f}")
