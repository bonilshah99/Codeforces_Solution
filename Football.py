s = input()
count =0
for i in range(len(s)-1):
	if s[i] == s[i+1]:
		count += 1
		if count >= 6:
			break
	else:
		count = 0

print('YES' if count>=6 else 'NO')
	
