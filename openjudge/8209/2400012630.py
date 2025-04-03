n,m=map(int,input().split())
days=[int(input()) for _ in range(n)]

def is_possible(arr,m,mid) :
    count=1
    current_sum=0
    for num in arr :
        if current_sum+num>mid :
            count+=1
            current_sum=num
            if num>mid :
                return False
        else :
            current_sum+=num
        if count>m :
            return False
    return count<=m

left=max(days)
right=sum(days)
result=right  

while left<=right :
    mid=(left+right)//2
    if is_possible(days,m,mid) :
        result=mid
        right=mid-1
    else :
        left=mid+1

print(result)