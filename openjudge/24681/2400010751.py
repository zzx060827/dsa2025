n=int(input())
def ways(s,l):
    num = 0
    if s in l:
        num=l[s]
    elif s==0:
        num = 1
        l[s] = num
    elif s<3:
        num=1
        l[s]=num
    elif s<5:
        num=ways(s-1,l)+ways(s-3,l)
        l[s] = num
    else:
        num=ways(s-1,l)+ways(s-3,l)+ways(s-5,l)
        l[s] = num
    return num
print(ways(n,{}))


