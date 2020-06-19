total = 0
arr=[]
for _ in range(int(input())):
	a,b = map(int,input().split())
	total += b -a
	arr.append(total) 
print(max(arr))