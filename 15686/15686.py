import sys
from itertools import combinations
I = sys.stdin.readline
N, M = map(int, I().split())
City = [[int(e) for e in I().split()] for _ in range(N)]
House = []
Chicken = []
for i in range(N):
    for j in range(N):
        if City[i][j] == 1:
            House.append((i,j))
        elif City[i][j] == 2:
            Chicken.append((i,j))
ans = N*2*len(House)*len(Chicken)
for m in range(1,M+1):
    for C in combinations(Chicken, m):
        Distance = 0
        for hx, hy in House:
            distance = N*2
            for cx, cy in C:
                distance = min(distance, abs(cx-hx)+abs(cy-hy))
            Distance += distance
        ans = min(ans, Distance)
print(ans)