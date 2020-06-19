n,k = map(int,input().split())
l = list(map(int,input().split()))
ans = []

m = l[k-1]

for item in l:
	if item >= m and item>0:
		ans.append(item)

print(len(ans))
