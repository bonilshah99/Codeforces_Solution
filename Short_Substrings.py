for _ in range(int(input())):
	s = input()
	n = len(s)
	x = ''
	x = s[0]
	i = 0
	for i in range(n-1):
		if i % 2 == 1:
			x += s[i]
	x += s[-1]
	print(x)
		

		
			
