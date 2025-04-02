def readpoly():
    x = list(map(int, input().split()))
    poly = [0] * 101
    for i in range(0, len(x)-2, 2):
        poly[x[i+1]] = x[i]
    return poly

def add(x, y):
    poly = [0] * len(x)
    for i in range(0, len(x)):
        poly[i] = x[i] + y[i]
    return poly

def mul(x, y):
    poly = [0] * 2 * len(x)
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            poly[i+j] += x[i] * y[j]
    return poly

def myprint(x):
    buf = []
    for i in reversed(range(len(x))):
        if x[i] == 0:
            continue;
        buf.append(''.join(['+' if len(buf) > 0 and x[i] > 0 else '',  #连接
                 str(x[i]) if i == 0 else '' if x[i]==1 else '-' if x[i]==-1 else str(x[i]), #系数
                 "" if i==0 else "x" if i==1 else "x^{}".format(i) #次方数
                            ]))
    print(''.join(buf))


if __name__ == "__main__":
    x = readpoly()
    y = readpoly()
    myprint(add(x,y))
    myprint(mul(x,y))


