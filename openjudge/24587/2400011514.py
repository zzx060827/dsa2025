def is_matched(s):
    stack = []
    # 括号配对表
    match = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return not stack  # 栈为空说明完全匹配

n = int(input())
for _ in range(n):
    line = input()
    print("YES" if is_matched(line) else "NO")
