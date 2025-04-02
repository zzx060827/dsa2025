r = int(input())
# 将小矩形切片,每一片宽度都是1,统计每个长度为1的列所有的切片的面积。由于互不重叠，所以可以直接相加。
s_for_each_column = [0]*r # x=i--x=i+1 切片的面积

s_all = 0
_ = int(input())
for i in range(_):
    l, t, w, h = map(int,input().split())
    for j in range(w):
        s_for_each_column[l+j] += h
    s_all += w*h

s_now = 0
for i in range(r):
    if s_now < (s_all+1)//2:
        s_now += s_for_each_column[i]
    else:
        if not s_for_each_column[i]: continue
        else:
            print(i)
            break
else:
    print(r)