import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<10 and 0<=y<10:
        return True
    return False
F = [I().strip() for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
d = ((-1,0),(1,0),(0,-1),(0,1))
Q = deque()
for i in range(10):
    for j in range(10):
        if F[i][j] == 'R':
            visited[i][j] = 1
        elif F[i][j] == 'L':
            L = i,j,0
Q.appendleft(L)
while Q:
    x, y, p = Q.pop()
    if F[x][y] == 'B':
        print(p-1)
        break
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and not visited[nx][ny]:
            visited[nx][ny] = 1
            Q.appendleft((nx,ny,p+1))