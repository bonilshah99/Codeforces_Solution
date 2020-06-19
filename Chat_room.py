s = input()
a = 'hello'
count,j = 0,0

for i in range(len(s)):
	if s[i] == a[j]:
		count += 1
		j += 1
	if count == 5:
		break

print('YES' if count == 5 else 'NO')

