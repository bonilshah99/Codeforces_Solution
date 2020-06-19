l = input().split()
n,k = list(map(int,l[0])),int(l[1])

for i in range(k):
	if n[-1] > 0 :
		n[-1] = n[-1] - 1
	else:
		n.pop(-1)

for item in n:
	print(item,end='')

 
