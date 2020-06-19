for _ in range(int(input())):
	s,d = map(int,input().split())

	print(min((s+d)//3,min(s,d)))


