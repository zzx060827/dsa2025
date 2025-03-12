#8211 0190
#这个题明显是错的，25.133*2>pi*4**2
'''from math import pi

def V(r):
	a=pi*r**2
	return a
N,F=map(int,input().split())
pies=[]
radium=list(map(int,input().split()))
for r in radium:
	size=V(r)
	pies.append(int(size*1000))
print(pies)
right=max(pies)+1
left=0
def f(x):
	s=0
	for i in range(N):
		size=pies[i]
		s+=(size//x)
	return s
while left<right:
	mid=(left+right+1)//2
	if f(mid)<F+1:
		right=mid-1
	else:
		left=mid
print(left/1000,f(left))'''



'''#8210 0200

L,N,M=map(int,input().split())
distance=[]
for _ in range(N):
	distance.append(int(input()))

def possibe_distance(d,min_stones):
	count=0
	curr_distance=0

	i=0
	while i <=N-1:

		if distance[i]>=curr_distance+d and L-distance[i]>=d:
			count+=1
			curr_distance=distance[i]
			
			i+=1
		else:
			i+=1
			
	if count>=min_stones:
		return True
left=1
right=L
min_stones=N-M
while left<right:
	mid=(left+right+1)//2

	if not possibe_distance(mid,min_stones):
		right=mid-1
	else:
		left=mid
print(left)'''


#66 0120
#非常奇怪的二分查找。下面代码不对
'''N,K=map(int,input().split())
cable=[]
for _ in range(N):
	x=float(input())
	cable.append(int(x*100))
def can_divied(x):
	s=0
	for length in cable:
		s+=length//x
	return s
if sum(cable)<K:
	print(0.00)
else:
	left=1
	right=max(cable)+1
	while left<=right:
		mid=left+(right-left)//2
		s=can_divied(mid)
		
		if s>=K:
			left=mid+1
			ans=mid
		else:
			right=mid-1
	print(f'{ans/100:.2f}')'''

# 0210 2442 memory limit excess
'''n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
	a,b,c,d=map(int,input().split())
	A.append(a)
	B.append(b)
	C.append(c)
	D.append(d)
dict={}
for i in range(n):
	for j in range(n):
		s=A[i]+B[j]
		lst=dict.get(s,[0,0])
		lst[0]+=1
		dict[s]=lst
for i in range(n):
	for j in range(n):
		s=-(C[i]+D[j])
		if s in dict:
			lst=dict[s]
			lst[1]+=1
			dict[s]=lst
ans=0
for key in dict:
	ans+=dict[key][0]*dict[key][1]
print(ans)'''
# 0220 12067 不会做
'''statistics={}
while True:
	n,k=map(int,input().split())
	if n==0 and k==0:
		break
	else:
		scores=[]
		
		
		correct=list(map(int,input().split()))
		total=list(map(int,input().split()))
		scores.append(correct)
		scores.append(total)
		statistics[(n,k)]=scores

for (n,k),scores in statistics.items():
	proportion=[(scores[0][i]/scores[1][i],i) for i in range(n)]
	proportion=sorted(proportion,key=lambda x:x[0])
	a=0
	b=0
	for i in range(k,n):
		ind=proportion[i][1]
		a+=scores[0][ind]
		b+=scores[1][ind]
	print(int(100*a/b))'''

#0230 22007 N皇后 accepted
'''def is_safe(board, row, col):
	# 检查当前位置是否安全
	# 检查同一列是否有皇后
	for i in range(row):
		if board[i] == col:
			return False
	# 检查左上方是否有皇后
	i = row - 1
	j = col - 1
	while i >= 0 and j >= 0:
		if board[i] == j:
			return False
		i -= 1
		j -= 1
	# 检查右上方是否有皇后
	i = row - 1
	j = col + 1
	while i >= 0 and j < N:
		if board[i] == j:
			return False
		i -= 1
		j += 1
	return True

def queen_dfs(board, row):
	if row == N:
		# 找到第b个解，将解存储到result列表中
		ans.append(''.join([str(x) for x in board]))
		return
	for col in range(N):
		if is_safe(board, row, col):
			# 当前位置安全，放置皇后
			board[row] = col
			# 继续递归放置下一行的皇后
			queen_dfs(board, row + 1)
			# 回溯，撤销当前位置的皇后,可有可无
			board[row]=0
N=int(input())
ans=[]
queen_dfs([0]*N,0)
if ans !=[]:
	for nums in ans:
		print(' '.join(nums))
else:
	 print("NO ANSWER")'''

#0240 1750 accepted 注意用递归的方法自己实现
'''def permutation(arr):
	if len(arr)==1:
		return [arr]
	else:
		result=[]
		n=len(arr)
		for i in range(n):
			curr=arr[i]
			rema=arr[:i]+arr[i+1:]
			for s in permutation(rema):
				result.append(curr+''.join(s))
		return result
s=input()
arr=list(s)
arr.sort()
result=permutation(arr)
for x in result:
	print(''.join(x))'''

#0250 1696 波兰表达式 没有给出答案应该取多少位，学习算法就好
'''def evaluate_polish(expression):
	stack = []
	operators = {'+', '-', '*', '/'}

	# 将表达式按空格分割并反转，方便从右向左处理
	tokens = expression.split()[::-1]

	for token in tokens:
		if token not in operators:
			# 如果是操作数，直接入栈
			stack.append(float(token))
		else:
			# 如果是运算符，弹出栈顶的两个操作数
			operand1 = stack.pop()
			operand2 = stack.pop()
			# 根据运算符进行计算，并将结果压入栈
			if token == '+':
				stack.append(operand1 + operand2)
			elif token == '-':
				stack.append(operand1 - operand2)
			elif token == '*':
				stack.append(operand1 * operand2)
			elif token == '/':
				stack.append(operand1 / operand2)

	# 最终栈中只剩下一个元素，即为表达式的值
	return stack[0]

# 测试用例
expression = input()
result = evaluate_polish(expression)
print(result)'''


#0260 22799 accepted 略
'''def f(n):
	if n==1:
		return 1
	if n==2:
		return 2
	else:
		return f(n-1)+f(n-2)
n=int(input())
print(f(n))'''
			
#0280 666 注意这个递归，比较巧妙，没做出来
# 递归思想 accepted
'''def put_apple(m, n):
	if m < 0 or n < 0:
		return -1
	if n == 1 or m == 0:
		return 1
	# 如果 苹果数量m 小于 盘子数量n,相当于 把m个苹果放到 m个盘子里
	elif m < n:
		return put_apple(m, m)
	# 如果 m >= n, 递归思想，等于有一个空盘子的放法，加上没有空盘的放法
	# 即 p(m,n) = p(m,n-1) + p(m-n,n)
	elif m >= n:
		return put_apple(m, n - 1) + put_apple(m - n, n)
t=int(input())
for _ in range(t):
	m,n=map(int,input().split())
	print(put_apple(m, n))#m个苹果 n个盘子'''

#0290 23660
#itertools的应用
'''from itertools import combinations


t=int(input())

for _ in range(t):
	count=0
	dict={i:0 for i in range(7)}
	l,nums=input().split(' ',maxsplit=1)
	lst=list(map(int,nums.split()))
	for i in range(int(l)+1):
		gen=combinations(lst,i)
		for tup in gen:
			if sum(tup)%7==0:
				count+=1
	print(count)'''

#0300 7622
#注意归并排序算法 nlogn accepted
'''def merge_sort_and_count(arr):
	if len(arr) <= 1:
		return arr, 0
	mid = len(arr) // 2
	left, left_inv = merge_sort_and_count(arr[:mid])
	right, right_inv = merge_sort_and_count(arr[mid:])
	merged, split_inv = merge_and_count(left, right)
	return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
	result = []
	inv_count = 0
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			inv_count += len(left) - i  # 因为left[i:]的所有元素都比right[j]大
	result.extend(left[i:])
	result.extend(right[j:])
	return result, inv_count

# 测试代码
n=int(input())
arr = list(map(int,input().split()))
sorted_arr, total_inv_count = merge_sort_and_count(arr)

print(total_inv_count)'''

#0310 22006 accepted
'''dic={0:'A',1:'B',2:'C'}
def operations(n,i,j):
	if n==1:
		print(dic[i]+'->'+dic[j])
		return
	else:
		k=3-i-j
		operations(n-1,i,k)
		print(dic[i]+'->'+dic[j])
		operations(n-1,k,j)
n=int(input())
operations(n,0,2)'''

#0320 24681 accepted 水题略
'''def f(n):
	if n<0:
		return 0
	elif n==0:
		return 1
	else:
		return f(n-1)+f(n-3)+f(n-5)
n=int(input())
print(f(n))'''

#0330 23937
#BFS做法
'''from collections import deque
N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
movement=[(1,0),(0,1)]
visited=set()
def legal(step):
	i,j=step
	if 0<=i<=N-1 and 0<=j<=N-1 and map[i][j]!=1 and step not in visited:
		return True
	else:
		return False
def bfs(map):
	queue=deque()
	start=(0,0)
	queue.append(start)
	visited.add(start)
	while queue:
		position=queue.popleft()
		if position==(N-1,N-1):
			return "Yes"
		for move in movement:
			dx,dy=move
			x,y=position
			next_step=(x+dx,y+dy)
			if legal(next_step):
				queue.append(next_step)
				visited.add(next_step)
			
	else:
		return "No"
result=bfs(map)
print(result)'''
#DFS方法
'''N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
movement=[(1,0),(0,1)]
visited=[[0]*N for _ in range(N)]
def legal(step):
	i,j=step
	if 0<=i<=N-1 and 0<=j<=N-1 and map[i][j]!=1 and not visited[i][j]:
		return True
	else:
		return False
def dfs(map,x,y):
	for move in movement:
		dx,dy=move
		next_step=(x+dx,y+dy)
		if next_step==(N-1,N-1):
			return 'Yes'
		else:
			if legal(next_step):
				visited[x][y]=1
				result=dfs(map,x+dx,y+dy)
				if result=="Yes":
					return "Yes"
				visited[x][y]=0
result=dfs(map,0,0)
if result:
	print(result)
else:
	print('No')'''

#0390 20983 简单的递归 ac
'''def f(n,k):
	if n==0:
		return 1
	elif k>n:
		return f(n,n)
	else:
		s=0
		for i in range(1,k+1):
			s+=f(n-i,i)
		return s
N=int(input())
print(f(N,N))'''

#0400 7617 ac 没什么好说的，简单
'''n=int(input())
nums=list(map(int,input().split()))
nums=sorted(nums,reverse=True)
k=int(input())
for i in range(k):
	print(nums[i])'''

#0410 24587 注意多检验一下栈为空的情况，别的没了，简单
'''n=int(input())

def parentheses_paired(s):
	stack=[]
	for char in s:
		
		if char=='(' or char=='[' or char=='{':
			stack.append(char)
		elif char==')':
			if stack:
				x=stack.pop()
				if x!='(':
					return 'NO'
			else:
				return 'NO'
		elif char==']':
			if stack:
				x=stack.pop()
				if x!='[':
					return 'NO'
			else:
				return 'NO'
		elif char=='}':
			if stack:
				x=stack.pop()
				if x!='{':
					return 'NO'
			else:
				return 'NO'
	if stack==[]:
		return 'YES'
	else:
		return 'NO'

info=[]
for _ in range(n):
	s=input()    
	info.append(s)
for s in info:
	print(parentheses_paired(s))'''


#0420 24588 请注意这里设计的判断是不是数字的函数
'''def is_number(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def calculate_postorder_expression(s):
	stack=[]
	for char in s:
		
		if is_number(char):
			stack.append(float(char))

		else:
			right=stack.pop()
			left=stack.pop()
			if char=='+':
				x=left+right
				stack.append(x)
			elif char=='-':
				x=left-right
				stack.append(x)
			elif char=='*':
				x=left*right
				stack.append(x)
			elif char=='/':
				x=left/right
				stack.append(x)
	return f'{stack[0]:.2f}'
n=int(input())
for _ in range(n):
	s=input().split()
	print(calculate_postorder_expression(s))'''

#0450 22086
# 对每个人，检查它前面还没出栈的人的顺序是否为逆序 自己输入都没问题，不知道哪里错了
#加了一个长度相等判断后ac，题目是有点坑的，我默认长度上没问题 ac
'''def can_be_popped(s0,s):
	n=len(s0)
	if len(s)!=n:
		return False
	else:
		if n==0:
			return False
		elif n==1:
			if s==s0:
				return True
			else:
				return False
		elif n>=2:	
			x=s[0]
			if x in s0:
				ind_x=s0.index(x)
			else:
				return False
			probe=101
			for i in range(1,n):
				if s[i] in s0:
					
					y=s0.index(s[i])
				else:
					return False
				if y<ind_x and y<probe:
					probe=y
				elif y<ind_x and y>probe:
					return False
			else:
				return can_be_popped(s0[:ind_x]+s0[ind_x+1:],s[1:])
		
s0=input()
while True:
	try:
		s=input()
	
		if can_be_popped(s0,s):
			print('YES')
		else:
			print('NO')
	except EOFError:
		break'''

#0460 24828 这里是一个队列的方法，还有非常好的分段，维护数组的方法，见知乎文章收藏 ac
'''from collections import deque
n,k=map(int,input().split())
nums=list(map(int,input().split()))
maxi=[]
mini=[]
def MaxSlidingWindows(nums,k):
	queue=deque()
	for i ,val in enumerate(nums):
		if queue and queue[0]<=i-k:
			queue.popleft()
		while queue and nums[queue[-1]]<val:
			queue.pop()
		queue.append(i)
		if i>=k-1:
			maxi.append(str(nums[queue[0]]))
	return maxi
def MinSlidingWindows(nums,k):
	queue=deque()
	for i ,val in enumerate(nums):
		if queue and queue[0]<=i-k:
			queue.popleft()
		while queue and nums[queue[-1]]>val:
			queue.pop()
		queue.append(i)
		if i>=k-1:
			mini.append(str(nums[queue[0]]))
	return mini
print(' '.join(MinSlidingWindows(nums,k)))

print(' '.join(MaxSlidingWindows(nums,k)))
'''

#0470 2250 水题 ac
'''while True:
	try:
		x=int(input())
		b_x=bin(x)[2:]
		print(b_x)
	except EOFError:
		break'''

#0480 24782 简单 ac
'''S=input()
stack=[]
for char in S:
	stack.append(char)
	if len(stack)>=3 and stack[-1]=='U':
		x=stack[-3]
		y=stack[-2]
		if x=="P" and y=="K":
			stack=stack[:-3]
print(''.join(stack))'''

#0480 5714 简单，ac
'''t=int(input())
for _ in range(t):
	n=int(input())
	lst=[]
	ans=0
	Flag=True
	for _ in range(n):
		type,val=map(int,input().split())
		if Flag:
			if type==1:
				lst.append(val)
			if type==2:
				if len(lst)==1:
					lst=[]
				else:
					if val==lst[0]:
						ans='Queue'
					else:
						ans="Stack"
					Flag=False
					
	print(ans)'''


#0490 5902 easy,ac
'''t=int(input())
for _ in range(t):
	n=int(input())
	lst=[]
	for _ in range(n):
		type,val=map(int,input().split())
		if type==1:
			lst.append(str(val))
		else:
			if val==0:
				lst=lst[1:]
			else:
				lst=lst[:-1]
	if lst:
		print(' '.join(lst))
	else:
		print('NULL')'''

#0500 22506 栈的思想，我们合并两字符括号
'''while True:
	try:
		s=input()
		stack=[]
		n=len(s)
		i=0
		while i<n:
			
			if s[i]=='/':
				if  i+1 >n-1 or s[i+1]!='*':
					print('False')
					break
				else:
					stack.append('{')
					i+=2
			elif s[i]=='*':
				if  not stack or i+1>n-1 or s[i+1]!='/' or stack[-1]!='{':
					print('False')
					break
				else:
					stack.pop()
					i+=2
			elif s[i]=='[' or s[i]=='(':
				stack.append(s[i])
				i+=1
			elif s[i]==')':
				if  stack and stack[-1]=='(':
					stack.pop()
					i+=1
				else:
					print('False')
					break
			elif s[i]==']':
				if stack and stack[-1]=='[':
					stack.pop()
					i+=1
				else:
					print('False')
					break
			
		else:
			if not stack:
				print('True')
			else:
				print('False')

	except EOFError:
		break'''


#0510 22067 简单 ac
'''stack=[]
min=20001

crucial={}
mini=[]
while True:
	try:
		command=input()
		if command[1]=='u':
			weight=int(command[5:])
			stack.append(weight)
			
			if weight<min:
				min=weight
			mini.append(min)
		elif command=='min':
			if stack:
				print(min)
		else:
			if stack:
				stack.pop()
				mini.pop()
				
				min=mini[-1]
	except EOFError:
		break'''

		
		
#00520 9199 
#注意利用字典存储在与不在的状态，防止查找浪费时间
'''from collections import deque
M,N=map(int,input().split())
vocabulary=list(map(int,input().split()))
cache=deque()
length=0
cnt=0
existence={i:False for i in range(1000001)}
for i in range(N):
	word=vocabulary[i]
	if existence[word]:
		pass
	else:
		existence[word]=True
		cnt+=1
		if length==M:
			dropped_word=cache.popleft()
			existence[dropped_word]=False
		cache.append(word)
		length=min(M,length+1)
print(cnt)'''

#0540 3190
#注意到pop操作不需要增加当前操作数，修改一下就好了 ac
'''n=int(input())
cnt=0
def dfs(stack,k):
	global cnt
	if k==n+1 and not stack:
		cnt+=1
		return
	elif k==n+1 and stack:
		stack.pop()
		dfs(stack,k)
		return
	elif k<n+1 and not stack:
		stack.append(k)
		dfs(stack,k+1)
		return
	elif k<n+1 and stack:
		tmp=stack[:]
		k0=k
		stack.append(k)
		dfs(stack,k+1)
		tmp.pop()

		dfs(tmp,k0)
		return
dfs([],1)
print(cnt)'''

#0550 3058
#主动考虑能不能用栈来做，遂得此解
'''N=int(input())
stack=[-1]
cnt=0
for _ in range(N):
	h=int(input())
	while stack and stack[-1]<=h:
		stack.pop()
	cnt+=len(stack)
	stack.append(h)
print(cnt)'''

#0560 25141
#做你想做的 设置好build_tree的出口即可 ac
'''class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
	
		
nodes=[]
while True:
	
	try:
		node=input()
		s=0
		for char in node:
			if char=='\t':
				s+=1
		nodes.append([s,node[-1]])
	except EOFError:
		break

def build_tree(nodes):
	if not nodes:
		return None
	if len(nodes)==1 and nodes[0][1]=='*':
		
		return None
	else:

		level,val=nodes[0]
		root=TreeNode(val)
		for i,node in enumerate(nodes[2:]):
			if node[0]==level+1:
				leftnode=build_tree(nodes[1:i+2])
				rightnode=build_tree(nodes[i+2:])
				break
		else:
			leftnode=build_tree(nodes[1:])
			rightnode=None
		root.left=leftnode
		root.right=rightnode
		return root
def preorder_traversal(root):
	if not root:
		return ''
	else:
		return root.val+preorder_traversal(root.left)+preorder_traversal(root.right)
def inorder_traversal(root):
	if not root:
		return ''
	else:
		return inorder_traversal(root.left)+root.val+inorder_traversal(root.right)
def postorder_traversal(root):
	if not root:
		return ''
	else:
		return postorder_traversal(root.left)+postorder_traversal(root.right)+root.val

root=build_tree(nodes)
print(preorder_traversal(root))
print(inorder_traversal(root))
print(postorder_traversal(root))'''

#0570 22158
#常规的，记得定义简单情况的返回
'''class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
		
while True:
	try:
		preorder=input()
		inorder=input()
		def build_tree(preorder,inorder):
			if not preorder:
				return None
			else:
				root_val=preorder[0]

				root=TreeNode(root_val)
				sepa=inorder.index(root_val)
				left_subtree_preorder=preorder[1:sepa+1]
				right_subtree_preorder=preorder[sepa+1:]
				left_subtree_inorder=inorder[:sepa]
				right_subtree_inorder=inorder[sepa+1:]
				root.left=build_tree(left_subtree_preorder,left_subtree_inorder)
				root.right=build_tree(right_subtree_preorder,right_subtree_inorder)
				return root

		def postorder(root):
			if not root:
				return ''
			else:
				return postorder(root.left)+postorder(root.right)+root.val
		root=build_tree(preorder,inorder)
		print(postorder(root))
	except EOFError:
		break'''

#0580 25140
#比较常规，没什么好说的 ac
'''from collections import deque
class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
n=int(input())


for _ in range(n):
	s=input()
	stack=[]
	for char in s:
		if ord(char)>96:
			node=TreeNode(char)
			stack.append(node)
		else:
			node=TreeNode(char)
			right=stack.pop()
			left=stack.pop()
			node.left=left
			node.right=right
			stack.append(node)
	root=stack[0]
	queue=deque()
	queue.append(root)
	traversal=[]
	while queue:
		node=queue.popleft()
		traversal.append(node.val)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	traversal=traversal[::-1]
	print(''.join(traversal))'''

#0590 4335
'''import heapq
class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
	def __lt__(self,other):
		return self.val<other.val
N=int(input())
heap=[]
for _ in range(N):
	node=TreeNode(int(input()))
	heapq.heappush(heap,node)
cost=0
while len(heap)>1:
	leftnode=heapq.heappop(heap)
	rightnode=heapq.heappop(heap)
	newnode=TreeNode(leftnode.val+rightnode.val)
	newnode.left=leftnode
	newnode.right=rightnode
	heapq.heappush(heap,newnode)
	cost+=newnode.val
print(cost)'''

#0750 25154
#下面代码的问题：一个点作为root出现时会磨灭曾经的数据，需要修改
#注意TreeNode默认传参的过程中会有问题，具体原理有待研究 ac
#破案了，自己坑自己，本质错误只有一个，就是第二行所指出的
class TreeNode:
	def __init__(self,val,children=[],parent=None,l=None,r=None):
		self.val=val
		self.children=children
		self.parent=parent
		self.l=l
		self.r=r
info=[]
while True:
	try:
		s=input().split()
		info.append(s)
	except EOFError:
		break

nodes_val={}
for s in info:
	root_val=s[0]
	children_val=s[1:]
	if root_val in nodes_val:
		root=nodes_val[root_val]

	else:
		root=TreeNode(root_val,children=[])
		nodes_val[root_val]=root
	for child_val in children_val:
		if child_val in nodes_val:
			child=nodes_val[child_val]
			child.parent=root
		else:
			child=TreeNode(child_val,children=[])
			nodes_val[child_val]=child
			child.parent=root

		root.children.append(child)
nodes=[nodes_val[val] for val in nodes_val]	
for node in nodes:
	if not node.parent:
		root=node
for node in nodes:
	if node.children:
		first_children=node.children[0]
		node.l=first_children
	if node.parent and node.parent.children[-1]!=node:
		k=node.parent.children.index(node)
		next_sibling=node.parent.children[k+1]
		node.r=next_sibling

def postorder_traversal(root):
	if not root:
		return ''
	else:
		return postorder_traversal(root.l)+postorder_traversal(root.r)+root.val


print(postorder_traversal(root))

