import sys
from collections import deque
I = sys.stdin.readline
N, M, K, X = map(int,I().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, I().split())
    G[A].append(B)
D = [-1]*(N+1)
D[X] = 0
Q = deque((X,))
while Q:
    u = Q.popleft()
    for v in G[u]:
        if D[v] == -1:
            D[v] = D[u]+1
            Q.append(v)
cnt = 0
for i in range(1,N+1):
    if D[i] == K:
        print(i)
        cnt += 1
if not cnt:
    print(-1)