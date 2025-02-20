p,e,i,d=map(int,input().split())
sum=p
while True:
    if (sum-e)%28==0 and (sum-i)%33==0:
        print(sum-d if sum>d else sum+21252-d)
        break
    sum+=23
