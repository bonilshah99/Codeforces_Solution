for _ in range(int(input())):
	a,b = map(int,input().split())

	if a<=b//2 or b<=a//2:
		print(max(a,b)**2)
	elif a==b :
		print((a*2)**2)
	else:
		print((min(a,b)*2)**2)