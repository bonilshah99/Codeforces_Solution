n,h = map(int,input().split())

l = list(map(int,input().split()))
count = 0

for i in l:
	if i>h:
		count += 2
	else:
		count += 1

print(count)