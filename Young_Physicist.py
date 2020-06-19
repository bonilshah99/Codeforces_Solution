X,Y,Z = 0,0,0
for _ in range(int(input())):
	x,y,z = map(int,input().split())
	X += x
	Y += y
	Z += z 

print('YES' if (X==0 and Y==0 and Z==0) else 'NO')