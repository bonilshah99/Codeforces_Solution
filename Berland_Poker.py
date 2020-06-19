for _ in range(int(input())):
	n,m,k = map(int,input().split())
	card = n/k
	if m>0:
		if card >= m:
			print(m)
		else:
			if (m-card)%(k-1) == 0:
				print(int((card) - ((m-card)//(k-1))))
			else:
				print(int((card) - ((m-card)//(k-1)) - 1 ))
	else:
		print('0')

