# 백준 11048번 이동하기
https://www.acmicpc.net/problem/11048
---

### 문제 해결 날짜
- 2022.04.28
---

### 코드 설명
- `dp[x][y]`는 (1,1)부터 (x,y)까지 이동하는 동안 얻을 수 있는 사탕의 최대개수이다.
- 가로로 이동한 후 세로로 이동하며 dp테이블을 업데이트한다. `즉, dp[1][1]~dp[1][M] 이동 후 dp[2][1]~dp[2][M]로 이동하는 식으로 이동하며 dp테이블을 업데이트한다.`
- 사탕은 음수개가 될 수 있으므로 `dp[x][y]`의 초기값은 (x,y)에 놓여진 사탕의 개수이다.
- `dp[x][y]는 dp[x][y]+max(dp[x-1][y],dp[x][y-1],dp[x-1][y-1])`이다.
---

### 소스코드
- 메모리 : 69464KB
- 시간 : 2432ms
```Python
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
```