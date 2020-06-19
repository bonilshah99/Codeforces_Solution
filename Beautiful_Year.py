s = int(input())
s += 1

while len(set(str(s))) != 4:
	s += 1

print(s)
