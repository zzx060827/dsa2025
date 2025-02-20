'''P0010:合并有序序列
查看提交统计提问
总时间限制: 1000ms 内存限制: 65536kB
描述
给定两个长度为n的从小到大排好序的整数序列，请用O(n)时间将其合并为一个新的有序序列。

输入
第1行是整数n
第2行是n个整数，从小到大排好序。
第3行是n个整数，从小到大排好序。

每行整数不超过100000个。所有整数非负，且不大于 200000
输出
一行，将输入中的两行整数合并为新的从小到大整数序列的结果
样例输入
4
2 8 12 19
1 3 4 10
样例输出
1 2 3 4 8 10 12 19 '''
n=int(input())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
i=0
j=0
ans=[]
while i<n and j<n :
    if num1[i]<num2[j]:
        ans.append(num1[i])
        i+=1
    else:
        ans.append(num2[j])
        j+=1
if i==n:
    for k in range(j,n):
        ans.append(num2[k])
else:
    for k in range(i,n):
        ans.append(num1[k])
for i in range(2*n-1):
    print(ans[i],end=' ')
print(ans[2*n-1])