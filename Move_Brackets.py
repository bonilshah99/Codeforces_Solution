for _ in range(int(input())):
	n = int(input())
	s = input()
	count = 0
	ans = 0

	for i in s:
		if i =="(":
			count += 1
		else:
			count -= 1
		if count<0:
			ans += 1
			count = 0

	print(count)