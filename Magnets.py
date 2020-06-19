n = int(input())
count = 1
a = input()

for i in range(n-1):
	b = input()
	if b!=a:
		count += 1
		a = b
print(count)


