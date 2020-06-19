n = int(input())
l = [int(x) for x in input().split()]
l.sort()
l.reverse()
m = sum(l)/2
r = 0
for i in range(n):
	r += l[i]
	if r > m:
		print(i+1)
		break
	if r==m and i==n-1:
		print(n)
		break
