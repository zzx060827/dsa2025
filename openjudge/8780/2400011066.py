from bisect import bisect_right
N=int(input())
h=list(map(int,input().split()))[::-1]
l=[]
for k in h:
    ind=bisect_right(l,k)
    if ind==len(l):
        l.append(k)
    else:
        l[ind]=min(l[ind],k)
print(len(l))
