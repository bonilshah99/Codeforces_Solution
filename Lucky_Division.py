s = int(input())
arr = [4,7,47,74,44,447,444,474,477,774,744,777]
flag = 0
for i in arr:
	if s%i == 0:
		flag = 1
print('YES' if flag==1 else 'NO')