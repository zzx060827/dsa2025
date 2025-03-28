# 注意到 $f(x)=x^{2}+x+1+\text{log}_{2}x$ 是单调递增的函数。
from math import log2
def f(x):
	return x**2 + x + 1 + log2(x)

while True: # 读入未知行数的数据
	try:
		y = int(input())
	except:
		break
	left = 2
	right = y**0.5 # 尽量让二分范围减小，这样子可以让浮点误差减小。
	while right - left > 0.000001:
		mid = 0.5 * (left + right)
		test = f(mid)
		if test > y:
			right = mid
		else:
			left = mid
	else:
		mid = 0.5 * (left + right)
		print(f'{mid:.4f}')
