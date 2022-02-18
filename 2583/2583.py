import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<M and 0<=y<N:
        return True
    return False
M, N, K = map(int, I().split())
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    b,a,d,c = map(int,I().split())
    for i in range(a,c):
        for j in range(b,d):
            visited[i][j] = 1
A = []
dx = (-1,1,0,0)
dy = (0,0,-1,1)
for i in range(M):
    for j in range(N):
        print(visited[i][j], end=" ")
    print()
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            ans = 0
            stack = deque()
            stack.append((i,j))
            while stack:
                x, y = stack.pop()
                visited[x][y] = 1
                ans += 1
                for k in range(4):
                    X = x+dx[k]
                    Y = y+dy[k]
                    if in_range(X,Y) and not visited[X][Y]:
                        stack.append((X,Y))
                        visited[X][Y] = 1
            A.append(ans)
A.sort()
print(len(A))
for a in A:
    print(a, end=" ")