for _ in range(int(input())):
	n,x = map(int,input().split())
	l = list(map(int,input().split()))
	flag = False
	if sum(l)%x != 0:
		print(n)
	else:
		for i in range(n//2):
			if l[i]%x != 0 or l[n-i-1]%x != 0:
				flag = True
				break

		if flag == False:
			print('-1')
		else:
			print(n-i-1)
