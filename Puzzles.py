n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
res = 100000000
for i in range(len(l)):
	x = l[i:n+i]
	if len(x) == n:
		ans = max(x) - min(x)
		res = min(ans,res)

print(res)
