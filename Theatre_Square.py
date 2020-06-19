from math import ceil 
n,m,a = map(int,input().split())
num = ceil(n/a) * ceil(m/a)
print(num)