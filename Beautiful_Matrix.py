matrix = []
for _ in range(5):
	matrix.append(list(map(int,input().split())))
row = 0
colunm = 0
for i in range(5):
	for j in range(5):
		if matrix[i][j] == 1:
			row = i
			colunm = j
			break
print(abs(row-2) + abs(colunm-2))