import sys
def zhan(a,b):
    lista=['']*len(a)
    top=-1
    n=True
    for i in b:
        if i in a:
            num=a.index(i)
            if num==0:
                a=a[1:]
            else:
                for j in a[:num]:
                    top+= 1
                    lista[top]=j
                a=a[1+num:]
        else:
            if top>=0:
                if i==lista[top]:
                    top-=1
                else:
                    n=False
                    break
            else:
                n=False
                break
    return n


# 输入部分
x = input() # 读取原始字符串x
while True:
    try:
        query = input()
        if len(query) ==len(x) and zhan(x,query):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break




def popsequence(x, seq):
    stack = []
    idx = 0  # 记录压入栈的字符位置
    for char in seq:    # 模拟压栈和出栈
        while idx < len(x) and (not stack or stack[-1] != char):        # 压栈：直到栈顶是目标字符
            stack.append(x[idx])
            idx += 1
        if stack and stack[-1] == char:
            stack.pop()  # 出栈
        else:# 如果栈顶不是当前要出栈的字符，说明不合法
            return "NO"
    if len(x)!=len(seq): return "NO"
    return "YES"
x = input()
result=[]
while True:
    try:
        seq = input()
        print(popsequence(x, seq))
    except EOFError:
        break