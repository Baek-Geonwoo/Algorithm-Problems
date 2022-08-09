# 백준 1405번 미친 로봇
https://www.acmicpc.net/problem/1405
---

### 문제 해결 날짜
- 2022.08.10
---

### 코드 설명
- DFS를 통해 해결하였다.
- visited는 가로 세로 2N+1 범위의 2차원 리스트이다.
- 로봇이 어떤 경로로 이동할 확률 p를 DFS를 통해 구하면서 총 N번 이동하는 데 성공했다면 ans에 p를 더한다.
- 중간에 방문한 칸이 2번 방문 되면 즉시 DFS를 종료한다.(이후로는 단순하지 않은 경로가 되기 때문)
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 3396 ms
```Python
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
```