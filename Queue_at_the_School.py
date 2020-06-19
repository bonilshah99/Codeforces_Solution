n,t = map(int,input().split())
l = list(input())
for i in range(t):
	j = 0
	while j<n-1:
		if l[j] == 'B' and l[j+1] == 'G':
			l[j],l[j+1] = 'G','B'
			j += 2
		else:
			j += 1
print(''.join(l))


