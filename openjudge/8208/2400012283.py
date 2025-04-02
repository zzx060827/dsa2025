r=int(input())
n=int(input())
lis=[]
for _ in range(n):
    l,t,w,h=(map(int,input().split()))
    lis.append((l,t,w,h))

def cal(k):
    sl=0
    sr=0
    for (l,t,w,h) in lis:
        if l+w<=k:
            sl+=w*h
        elif l<k:
            sl+=h*(k-l)
            sr+=h*(w+l-k)
        else:
            sr+=w*h
    return sl,sr


low=0
high=r
rek=r

while low<= high:
    mid=(low+high)//2
    sl,sr=cal(mid)
    if sl>=sr:
        rek=mid
        high=mid-1
    else:
        low=mid+1

besl,besr=cal(rek)
mincha=besl-besr

result=rek
for k in range(rek+1,r+1):
    le,ri=cal(k)
    if (le-ri)==mincha:
        result=k
    else:
        break
print(result)