import random
class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next
class LinkList:
	def __init__(self,lst):
		self.head = Node(lst[0])
		p = self.head
		L = len(lst)
		for i in range(1,L):
			node = Node(lst[i])
			p.next = node
			p = p.next
	def loopExists(self):
		a = self.head
		b = self.head
		try:
			while True:
				a = a.next
				b = b.next.next
				if a is b:
					return "True"
		except Exception:
			return "False"
				
while True:
	try:
		n,m = map(int,input().split())
	except:
		break
	a = [i for i in range(n+10)]
	random.shuffle(a)
	lst  = LinkList(a)
	if m == 1:
		if n > 10:
			pos = random.randint(0,n-5)
		else:
			pos = 0
		p = lst.head
		q = p
		for i in range(pos):
			q = q.next
		last = None
		while p is not None:
			last = p
			p = p.next
		last.next = q
	print(lst.loopExists())