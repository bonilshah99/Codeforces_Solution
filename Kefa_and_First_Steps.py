n = int(input())
l = list(map(int,input().split()))
count = 1
arr = []
if len(l) == 1:
	print('1')
else:
	for i in range(n-1):
		if l[i+1] >= l[i]:
			count += 1
			arr.append(count)
		else:
			count = 1
			arr.append(1)

	print(max(arr))


