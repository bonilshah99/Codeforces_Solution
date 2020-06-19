for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	l.sort()
	flag = 0
	even = 0
	odd = 0

	for i in l:
		if i%2 == 0:
			even += 1
		else:
			odd += 1

	if even%2 == 0 and odd%2 == 0:
		print('YES')
	else:
		for j in range(1,n):
			if abs(l[j] - l[j-1]) == 1:
				print('YES')
				flag = 1
				break

		if flag == 0:
			print('NO')
