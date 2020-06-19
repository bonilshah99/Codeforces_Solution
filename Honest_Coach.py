for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	arr = []

	for i in range(n):
		for j in range(i+1,n):
			arr.append(abs(l[i] - l[j]))


	print(min(arr))

