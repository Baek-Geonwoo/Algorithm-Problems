# 백준 2468번 안전 영역
https://www.acmicpc.net/problem/2468
---

### 문제 해결 날짜
- 2022.04.29
---

### 코드 설명
- 비가 아예 안올수도 있고, 이 경우는 가장 낮은 지점-1 만큼의 비가 내린 것과 같으므로 비가 내리는 양은 가장 낮은 지점-1부터 가장 높은 지점-1까지로 한다.(가장 높은 지점이 잠기면 어차피 그때 안잠긴 영역은 0이므로)
- 각각의 비의 양에 대해서 visited를 각각 생성하여 bfs로 안전 영역의 개수를 구한 후 ans를 업데이트하여 안전 영역의 최대 개수를 구한다.
---

### 소스코드
- 메모리 : 32436KB
- 시간 : 1340ms
```Python
import sys
from collections import deque
def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
input = sys.stdin.readline
def BFS(x,y,rain):
    Q = deque(((x,y),))
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and not visited[nx][ny] and M[nx][ny] > rain:
                visited[nx][ny] = 1
                Q.append((nx,ny))
d = (-1,0), (1,0), (0,-1), (0,1)
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(max(0,min(min(M))-1),max(max(M))):
    visited = [[0]*N for _ in range(N)]
    land = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and M[i][j] > r:
                land += 1
                BFS(i,j,r)
    ans = max(ans, land)
print(ans)
```