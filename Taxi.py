n = int(input())
l = list(map(int,input().split()))

three = l.count(3)
two = l.count(2)
one = l.count(1)

ans = n - one - two
one -= three
m = two*2
if one>0:
    m += one
 
ans += m // 4
 
if m%4:
    ans += 1
print(ans)

