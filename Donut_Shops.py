for _ in range(int(input())):
	a,b,c = map(int,input().split())

	if a<c:
		ans1 = 1
	else:
		ans1 = -1

	if a*b<=c:
		ans2 = -1
	else:
		ans2 = b

	print(f'{ans1} {ans2}')