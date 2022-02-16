import sys
from collections import deque
I = sys.stdin.readline
N = int(I())
M = int(I())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, I().split())
    G[a].append(b)
    G[b].append(a)
stack = deque([1])
visited = [False]*(N+1)
ans = -1 #1번 컴퓨터를 제외해야 하므로
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        ans += 1
        stack.extend(reversed(G[v]))
print(ans)