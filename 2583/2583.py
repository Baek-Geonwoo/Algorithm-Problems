import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<M and 0<=y<N:
        return True
    return False
M, N, K = map(int, I().split())
visited = [[False]*N for _ in range(M)]
for _ in range(K):
    b,a,d,c = map(int,I().split())
    for i in range(a,c):
        for j in range(b,d):
            visited[i][j] = True
A = []
dx = (-1,1,0,0)
dy = (0,0,-1,1)
for i in range(M):
    for j in range(N):
        ans = 0
        if not visited[i][j]:
            stack = deque([(i,j)])
            while stack:
                x, y = stack.pop()
                if not visited[x][y]:
                    visited[x][y] = True
                    ans += 1
                    for i in range(4):
                        X = x+dx[i]
                        Y = y+dy[i]
                        if in_range(X,Y):
                            stack.appendleft((X,Y))
            A.append(ans)
A.sort()
print(len(A))
for a in A:
    print(a, end=" ")