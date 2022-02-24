# 백준 16948번 데스 나이트
https://www.acmicpc.net/problem/16948
---

### 문제 해결 날짜
- 2021.02.25
---

### 코드 설명
- 시작지점과 0을 Q에 넣고 Q가 빌 때까지 NxN 체스판을 BFS탐색한다.
- ans에 데스나이트가 출발지점부터 도착지점까지 움직여야 하는 최소 횟수를 저장한다.(ans는 시작지점은 이미 방문한 것으로 간주하기 때문에  결코 ```N**2번 이상 이동할 수 없다. 따라서 ans의 초기값은 N**2```이다.)
- m은 해당 칸까지 데스 나이트가 이동한 횟수이다.
- 데스 나이트가 도착지점에 도착하면 ans =  min(ans, m)으로 초기화하고, continue한다.
- BFS 탐색이 끝났을 때 만약 ans가 초기값 그대로라면 도착지점까지 이동할 수 없다는 것이므로 -1을 출력한다. 아니라면 ans를 출력한다.
---

### 소스코드
- 메모리 : 32404KB
- 시간 : 124ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False
N = int(I())
sx, sy, ex, ey = map(int, I().split())
visited = [[0]*N for _ in range(N)]
d = (-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)
Q = deque(((sx,sy,0),))
visited[sx][sy] = 1
ans = N**2
reached = False
while Q:
    x, y, m = Q.pop()
    if x == ex and y == ey:
        ans = min(ans, m)
        reached = True
        continue
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and not visited[nx][ny]:
            Q.appendleft((nx,ny,m+1))
            visited[nx][ny] = 1
print(ans) if reached else print(-1)
```