import sys
from collections import deque
I = sys.stdin.readline
N, M = map(int, I().split())
S, E = map(int, I().split())
T = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, I().split())
    T[x].append(y)
    T[y].append(x)
Q = deque(((S,0),))
visited = [0]*(N+1)
visited[S] = 1
ans = abs(S-E)
while Q:
    X, t = Q.pop()
    if X == E:
        ans = min(ans, t)
        continue
    if T[X]:
        for i in T[X]:
            if not visited[i]:
                Q.appendleft((i,t+1))
                visited[i] = 1
    for d in range(-1,2,2):
        if 1<=X+d<=N and not visited[X+d]:
            Q.appendleft((X+d,t+1))
            visited[X+d] = 1
print(ans)