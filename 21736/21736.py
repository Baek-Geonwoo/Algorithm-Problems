import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
C = [I().strip() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
stack = deque()
for i in range(N):
    for j in range(M):
        if C[i][j] == 'I':
            stack.append((i,j))
            break
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while stack:
    x, y = stack.pop()
    visited[x][y] = True
    if C[x][y] == 'X':
        continue
    if C[x][y] == 'P':
        ans += 1
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if in_range(X,Y):
            if visited[X][Y] == True: continue
            stack.append((X,Y))
if not ans:
    print("TT")
else:
    print(ans)