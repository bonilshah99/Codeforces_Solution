k,n,w = map(int,input().split())
cost = 0
for i in range(1,w+1):
	cost += (i*k)

print(cost-n if cost>=n else '0')