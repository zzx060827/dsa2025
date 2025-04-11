while True: #读入组数未知的数据
	try:
		n, k = map(int, input().split())
	except:
		exit(0)
	"""N划分成K个正整数。""" # 泛化问题：dp[k][n]表示n划分成k个正整数之和的划分数目，记作Q(n, k)
	dp = [[0] * (n + 1) for _ in range(k + 1)]
	for col in range(1, n + 1):
		dp[1][col] = 1
	for row in range(2, k + 1):
		for col in range(row, n + 1):
			dp[row][col] = dp[row - 1][col - 1] + dp[row][col - row] # 关系：Q(n, k) = Q(n - 1, k - 1) + Q(n - k, k)，其中第一项表示有一个正整数为1后问题转化的结果；第二项表示没有任何正整数为1，因此可以把每一个划分出的正整数都都减掉1来考虑。
	print(dp[-1][-1])
	"""N划分成若干个不同的正整数""" # 泛化问题：dp[k][n]表示n划分成若干个不同且不超过k的正整数之和的划分数目
	# dp = [[0] * (n + 1) for _ in range(n + 1)]
	# dp[0][0] = 1
	# for row in range(1, n + 1):
	# 	for col in range(0, n + 1):
	# 		if col - row >= 0:
	# 			dp[row][col] = dp[row - 1][col] + dp[row - 1][col - row] # 关系：Q(n, k) = Q(n, k - 1) + Q(n - k, k - 1)，其中第一项表示不使用新可用的正整数k；第二项表示使用了最新可用的正整数k。
	# 		else:
	# 			dp[row][col] = dp[row - 1][col] # 注意：列表支持负数索引。
	# print(dp[-1][-1])
	# 现在进行空间优化，因为注意到我们每一次只需要用到前一行的结论：
	dp = [0] * (n + 1)
	dp[0] = 1
	for k in range(1, n + 1):
		for i in range(n, k - 1, -1): # 必须从大到小遍历，否则相当于dp[row - 1][col - row]的数据会被覆盖掉。
			dp[i] += dp[i - k]
	print(dp[-1])
	"""N划分成若干个奇正整数之和""" # 泛化问题：dp[n]表示n划分成若干个正奇数的和的方法数。
	dp = [1] * (n + 1)
	for k in range(3, n + 1, 2): # k表示可以使用的最大正奇数。
		for i in range(0, n + 1 - k):
			dp[i + k] += dp[i] # 关系：与92题类似，不过这次只能用奇数。
	print(dp[-1])
