import sys
from collections import deque
I = sys.stdin.readline
N, M = map(int, I().split())
C = [I().strip() for _ in range(N)]
stack = deque()
for i in range(N):
    for j in range(M):
        if C[i][j] == 'I':
            stack.append((i,j))
            break
visited = [[0]*M for _ in range(N)]
ans = 0
dx = (-1,1,0,0)
dy = (0,0,-1,1)
while stack:
    x, y = stack.pop()
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<N and 0<=Y<M and not visited[X][Y]:
            if C[X][Y] != 'X':
                if C[X][Y] == 'P':
                    ans += 1
                visited[X][Y] = 1
                stack.append((X,Y))
print(ans) if ans else print("TT")