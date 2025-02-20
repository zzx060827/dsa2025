def indexKMP(S, P):
    i=0                     #P的读写头
    j=0                     #S的读写头
    part=partial(P)         #计算P的partial
    while i<len(P) and j<len(S):
        if P[i] == S[j]:    #两个读写头下的字符相等
            i += 1
            j += 1
        else:               #不等
            if i==0:
                j += 1
            i = part[i]
    else:
        if i == len(P):     #找到了一个匹配
            return j-i
        else:
            return None

