R = int(input())  
N = int(input())  

rectangles = []
total_area = 0
for _ in range(N):
    L, T, W, H = map(int, input().split())
    rectangles.append((L, L + W, W,H)) 
    total_area += W * H

def get_left_area(x):
    left_area = 0
    for L, R, W, H in rectangles:
        if R <= x:
            left_area+=W*H
        else:
            if L < x:
                left_area+=(x-L)*H
    return left_area

def check(x):
    left_area  = get_left_area(x)
    right_area = total_area - left_area
    return left_area >= right_area

l,r =0,R
while l<r:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid+1

ans = l

while get_left_area(ans) == get_left_area(ans+1)  and ans+1 <= R:
    ans += 1
print(ans)