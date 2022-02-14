import sys
from collections import deque
I = sys.stdin.readline
def DFS(x,y):
    visited = [[False]*N for _ in range(N)]
    m = M[x][y]
    Q = deque([[x,y]])
    while Q:
        if visited[N-1][N-1]:
            return True
        x, y = Q.pop()
        m = M[x][y]
        for i in range(2):
            X, Y = x+m*dx[i], y+m*dy[i]
            if 0<=X<N and 0<=Y<N:
                if not visited[X][Y]:
                    Q.append([X,Y])
                    visited[X][Y] = True
    return False

N = int(I())
M = [list(map(int,I().split())) for _ in range(N)]
dx = [0,1]
dy = [1,0]
if DFS(0,0):
    print("HaruHaru")
else:
    print("Hing")