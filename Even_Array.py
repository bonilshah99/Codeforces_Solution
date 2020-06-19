for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	ecount = 0
	ocount = 0

	for i in range(n):
		if i%2 ==0 and l[i]%2 == 0:
			continue
		elif i%2 == 1 and l[i]%2 == 1:
			continue
		elif l[i]%2 == 0:
			ecount += 1
		else:
			ocount += 1

	if ecount == 0 and ocount == 0:
		print('0')
	elif ecount == ocount:
		print(ecount)
	else:
		print('-1')
