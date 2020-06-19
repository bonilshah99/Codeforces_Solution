a = int(input())
b = int(input())
c = int(input())

m = 0

if a+b+c>m:
	m = a+b+c
if a*b*c>m:
	m = a*b*c
if (a+b)*c>m:
	m = (a+b)*c
if a*(b+c)>m:
	m = a*(b+c)
if (a*b)+c>m:
	m = (a+b)*c
if a+(b*c)>m:
	m = a*(b+c)

print(m)

