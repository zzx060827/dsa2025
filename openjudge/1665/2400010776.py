def f(x):
    if x%2==1:
        return 0
    elif x==2:
        return 3
    elif x==0:
        return 1
    else:
        s=0
        for i in range(x//2):
            s+=2*f(2*i)
        return s+f(x-2)
while input:
    n=int(input())
    if n!=-1:
        print(f(n))
    else:
        break