import sys
def inRange(x,y):
    if 1<=x<=N and 1<=y<=M:
        return True
    return False
d = (-1,0), (0,-1), (-1,-1)
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [0] + [[0]+list(map(int,input().split())) for _ in range(N)]
for x in range(1,N+1):
    for y in range(1,M+1):
        m = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if inRange(nx,ny):
                m = max(m, dp[nx][ny])
        dp[x][y] += m
print(dp[N][M])