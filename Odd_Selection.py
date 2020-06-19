for _ in range(int(input())):
	n,x = map(int,input().split())
	l = list(map(int,input().split()))
	odd = 0
	even = 0

	for j in l:
			if j%2 == 1:
				odd += 1
			else:
				even += 1

	if odd == 0:
		print('No')
	elif even==0:
		if x%2==0:
			print('No')
		else:
			print('Yes')
	elif n==x:
		print('No' if odd%2==0 else 'Yes')
	else:
		if even >= x:
			print("Yes")
		else:
			temp = x - even
			if (temp)%2 == 0:
				if odd >= (temp):
					print('Yes')
				else:
					print('No')
			else:
				print('Yes')
