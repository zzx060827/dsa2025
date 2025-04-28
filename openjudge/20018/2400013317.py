def mergesort(a):
    ans=i=j=s=0
    if len(a)<=1:
        return 0
    left,right=a[:len(a)//2],a[len(a)//2:]
    ans+=mergesort(left)
    ans+=mergesort(right)
    a.clear()
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            a.append(right[j])
            s+=i
            j+=1
        else:
            a.append(left[i])
            i+=1
    if i<len(left):
        a+=left[i:]
    while j<len(right):
        a.append(right[j])
        s+=i
        j+=1
    return ans+s
while True:
    try:
        s=input()
        if s=='':
            continue
        n=int(s)
        a=[int(input()) for _ in range(n)]
        print(mergesort(a))
    except EOFError:
        break
