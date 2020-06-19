n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

p = p[1:]
q = q[1:]

res = set(p+q)
print('I become the guy.' if len(res) == n else 'Oh, my keyboard!')