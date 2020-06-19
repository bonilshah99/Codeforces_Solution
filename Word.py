s = input()
lower = 0
upper = 0

for item in range(len(s)):
	if s[item].islower():
		lower += 1
	else:
		upper += 1

print(s.lower() if lower>=upper else s.upper())