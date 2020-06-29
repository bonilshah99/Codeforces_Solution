n = int(input())
a = [None] * n
b = [None] * n 
count = 0
for i in range(n):
	x,y = map(int,input().split())
	a[i] = x
	b[i] = y

for i in range(n):
	for j in range(n):
		if a[i] == b[j] and i!=j:
			count += 1

print(count)
