s = input()
s = s.lower()
ans = ''
for item in s:
	if item not in 'aeiouy':
		ans += '.' + item
print(ans)