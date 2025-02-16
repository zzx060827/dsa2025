def indexOmn(S, P):
    i=0                     #P的读写头
    j=0                     #S的读写头
    while i<len(P) and j<len(S):
        if P[i] == S[j]:    #两个读写头下的字符相等
            i += 1
            j += 1
        else:               #不等
            j = j - i + 1   #把P右移一格，重新比较
            i = 0
    else:
        if i == len(P):     #找到了一个匹配
            return j-i
        else:
            return None

