n = int(input())
l = list(map(int,input().split()))

for item in range(1,n+1):
	print(l.index(item)+1,end=' ')