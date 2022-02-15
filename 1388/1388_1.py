import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
F = [list(I().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0,1]
dy = [1,0]
stack = deque([[0,0]])
visited[0][0] = True
ans = 1
while stack:
    x, y = stack.pop()
    for i in range(2):
        X = x+dx[i]
        Y = y+dy[i]
        if in_range(X,Y):
            if not visited[X][Y]:
                stack.append([X,Y])
                visited[X][Y] = True
                i = X-int(F[X][Y]=='|')
                j = Y-int(F[X][Y]=='-')
                if in_range(i,j):
                    if F[X][Y] != F[i][j]:
                        ans += 1
                else:
                    ans += 1
print(ans)