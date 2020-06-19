x = input().lower()
y = input().lower()
l =[x,y]
l.sort()
if x==y:
	print(0)
elif l[0] == x:
	print(-1)
else:
	print(1)