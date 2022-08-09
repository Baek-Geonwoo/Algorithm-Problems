import sys
input = sys.stdin.readline
d = (0,1), (0,-1), (1,0), (-1,0)

def dfs(move, p, x, y):
    global ans
    if visited[x][y] == 2:
        return
    if move == N:
        ans += p
        return
    for i in range(4):
        dx, dy = d[i]
        nx = x + dx
        ny = y + dy
        visited[nx][ny] += 1
        dfs(move+1, p*D[i], nx, ny)
        visited[nx][ny] -= 1

D = [0]*4
N, *D = map(int, input().split())
if not D[0]*D[1] + D[2]*D[3]:
    print(1.0)
    sys.exit()
D = [e/100 for e in D]
visited = [[0]*(2*N+1) for _ in range(2*N+1)]
ans = 0
visited[0][0] = 1
dfs(0, 1, 0, 0)
print(ans)