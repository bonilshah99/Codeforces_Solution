for _ in range(int(input())):
	s = input()
	one = 0
	zero = 0

	for i in s:
		if i == '0':
			zero += 1
		else:
			one += 1

	ans = min(one,zero)	

	print('DA' if ans%2 == 1 else 'NET')

