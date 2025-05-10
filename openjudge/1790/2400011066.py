from math import log2
while True:
    m,n=map(int,input().split())
    if m==n==0:
        break
    k=int(log2(n/m))
    end=m*(2**k)+2**k-1
    if n>=end:
        print(2**(k+1)-1)
    else:
        print(2**k+n-m*(2**k))
