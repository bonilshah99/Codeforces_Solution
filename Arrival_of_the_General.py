n = int(input())
l = list(map(int,input().split()))

big = l.index(max(l))

small = max([i for i, x in enumerate(l) if x == min(l)])

ans = big

if big>small:
	ans += (n-small-2)
else:
	ans += (n-small-1)
print(ans)
