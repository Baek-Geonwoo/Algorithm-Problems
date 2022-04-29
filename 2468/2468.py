import sys
from collections import deque
def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
input = sys.stdin.readline
def BFS(x,y,rain):
    Q = deque(((x,y),))
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and not visited[nx][ny] and M[nx][ny] > rain:
                visited[nx][ny] = 1
                Q.append((nx,ny))
d = (-1,0), (1,0), (0,-1), (0,1)
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(max(0,min(min(M))-1),max(max(M))):
    visited = [[0]*N for _ in range(N)]
    land = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and M[i][j] > r:
                land += 1
                BFS(i,j,r)
    ans = max(ans, land)
print(ans)