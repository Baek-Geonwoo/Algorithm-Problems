import sys
from collections import deque
input = sys.stdin.readline
def in_range(x,y):
    if 0<=x<R and 0<=y<C:
        return True
    return False

def bfs(x,y):
    Q = deque()
    Q.appendleft((x,y))
    while Q:
        x, y = Q.pop()
        cnt = 0
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and G[nx][ny] == '.':
                if not visited[nx][ny]:
                    Q.append((nx,ny))
                cnt += 1
        if cnt == 1:
            return True
        visited[x][y] = cnt

d = (1,0), (-1,0), (0,1), (0,-1)

R, C = map(int, input().split())
G = [input().rstrip() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dots = 0
for x in range(R):
    for y in range(C):
        if G[x][y] == '.':
            dots += 1
            if not visited[x][y] and bfs(x,y):
                print(1)
                sys.exit()
print(0)