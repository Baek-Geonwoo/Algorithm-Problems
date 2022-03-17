import sys
I = sys.stdin.readline
N, M = map(int,I().split())
B = [tuple(map(int,I().split())) for _ in range(N)]
B.sort(key= lambda x: (x[1], -x[0]))
ans = 2e32
mass = 0
P, price = 0, 0
for m, p in B:
    if price < p:
        price = p
        P = 0
    mass += m
    P += p
    if mass >= M:
        ans = min(ans, P)
if mass < M:
    print(-1)
else:
    print(ans)