n = int(input())
l = list(map(int,input().split()))
def mod(i):
	return i%2

ans = list(map(mod,l))
print(ans.index(1)+1 if ans.count(1) == 1 else ans.index(0)+1)

