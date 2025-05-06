scores = list(map(float,input().split()))
scores.sort()
n = len(scores)
excellentN= int(n * 0.6) + (1 if n * 0.6 > int(n * 0.6) else 0)
border_value = scores[n-excellentN]

l, r, ans = 1, 10**9, 10**9
while l<=r:
    mid = (l+r)//2
    a = mid/10**9
    adjusted =  a*border_value+1.1**(a*border_value)
    if adjusted >=85:
        ans = mid
        r=mid-1
    else:
        l=mid+1

print(ans)