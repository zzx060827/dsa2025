n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

if n==1:
    result=a[0]
elif n==2:
   result=max(a[0]+b[1],b[0]+a[1])
else:
 leftmax=[[0,0] for i in range(n-1)]
 for i in range(n-1):
    if i==0:
        leftmax[i][1]=b[0]
        leftmax[i][0]=a[0]
    else:
        leftmax[i][1]=max(leftmax[i-1][1]+b[i],leftmax[i-1][0]+c[i])
        leftmax[i][0]=max(leftmax[i-1][1]+a[i],leftmax[i-1][0]+b[i])

 result=max(leftmax[n-2][0]+b[n-1],leftmax[n-2][1]+a[n-1])
print(result)
        
