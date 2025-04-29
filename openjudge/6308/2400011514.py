case = 1
while True:
    s = input().strip()
    if s == '#':
        break
    stack = [(0, 0)]  # 每个元素保存(转换后的深度, 子节点数目)
    h1 = 0
    h2 = 0
    for c in s:
        if c == 'd':
            parent_depth, parent_child = stack[-1]
            order = parent_child + 1
            current_depth = parent_depth + order
            if current_depth > h2:
                h2 = current_depth
            # 更新父节点的子节点数目
            stack[-1] = (parent_depth, parent_child + 1)
            # 添加新节点到栈中
            stack.append((current_depth, 0))
            # 计算当前原树深度
            current_h1 = len(stack) - 1
            if current_h1 > h1:
                h1 = current_h1
        else:  # 'u'
            stack.pop()
    print(f"Tree {case}: {h1} => {h2}")
    case += 1