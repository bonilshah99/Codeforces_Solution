x = 0
for _ in range(int(input())):
	s = input()
	if s == '++X' or s == 'X++':
		x += 1
	else:
		x -= 1
print(x)