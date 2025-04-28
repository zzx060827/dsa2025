s_input = input().strip()
parts = s_input.split(',')
if len(parts) != 3:
    print(-1)
else:
    S, S1, S2 = parts
    len1 = len(S1)
    len2 = len(S2)
    
    # 查找S1的所有起始位置
    s1_starts = []
    for i in range(len(S) - len1 + 1):
        if S[i:i+len1] == S1:
            s1_starts.append(i)
    
    # 查找S2的所有起始位置
    s2_starts = []
    for j in range(len(S) - len2 + 1):
        if S[j:j+len2] == S2:
            s2_starts.append(j)
    
    # 判断是否存在符合条件的S1和S2
    if not s1_starts or not s2_starts:
        print(-1)
    else:
        min_r1 = min([i + len1 for i in s1_starts])
        max_s2 = max(s2_starts)
        if max_s2 >= min_r1:
            print(max_s2 - min_r1)
        else:
            print(-1)