import sys
from collections import deque, defaultdict
d = (-1,0), (1,0), (0,-1), (0,1)
def input():
    return [int(e) for e in sys.stdin.readline().split()]
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
def bfs(n,x,y):
    V = [(x,y)]
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    while Q:
        x, y = Q.pop()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and A[nx][ny] == n:
                Q.appendleft((nx, ny))
                V.append((nx,ny))
                visited[nx][ny] = 1
    return V
N, M = input()
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
S = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            S.append(bfs(A[i][j],i,j))
cnt = 0
for s in S:
    x, y = s[0]
    n = A[x][y]
    kind = defaultdict(int)
    for x,y in s:
        if B[x][y] != n:
            kind[B[x][y]] += 1
    if len(kind) == 0:
        continue
    elif len(kind) >= 2 or kind[B[x][y]] != len(s):
        cnt = 2
        break
    elif len(kind) == 1:
        cnt += 1
if cnt <= 1:
    print('YES')
else:
    print('NO')