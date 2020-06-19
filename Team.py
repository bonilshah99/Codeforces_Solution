count = 0
for _ in range(int(input())):
	l = input().split()
	if l.count('1') >= 2:
		count += 1
print(count)