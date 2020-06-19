from math import ceil
for _ in range(int(input())):
	x,y = map(int,input().split())
	l = ceil((x*y)/2) 
	print(l)