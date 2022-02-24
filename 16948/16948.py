import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
N = int(I())
sx, sy, ex, ey = map(int, I().split())
visited = [[0]*N for _ in range(N)]
d = (-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)
Q = deque(((sx,sy,0),))
visited[sx][sy] = 1
ans = N**2
while Q:
    x, y, m = Q.pop()
    if x == ex and y == ey:
        ans = min(ans, m)
        continue
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and not visited[nx][ny]:
            Q.appendleft((nx,ny,m+1))
            visited[nx][ny] = 1
print(ans) if ans != N**2 else print(-1)