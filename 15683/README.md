# 백준 15683번 감시
https://www.acmicpc.net/problem/15683
---

### 문제 해결 날짜
- 2021.03.14
---

### 코드 설명
- d는 상하좌우 방향, ```D[n]은 n번 CCTV의 각 방향에 따른 d 인덱스 튜플```
- 각 CCTV에 대하여 CCTV 위치, CCTV 번호, CCTV 방향인덱스를 튜플(x,y,c,n)로 Direction에 저장
- Direction의 크기가 CCTV 개수와 같아지면 Direction에 저장된 CCTV 방향대로 CCTV를 배치했을 때 사각지대의 크기(cnt)를 구하여 ans = min(ans, cnt)로 ans 초기화
---

### 소스코드
- 메모리 : 32512KB
- 시간 : 4028ms
```Python
import sys
from copy import deepcopy
from collections import deque
def dfs(Direction):
    global ans
    if len(Direction) == len(CCTV):
        O = deepcopy(Office)
        for x, y, c, n in Direction:
            for i in D[c][n]:
                dx, dy = d[i]
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not in_range(nx,ny):
                        break
                    if O[nx][ny] == 0:
                        O[nx][ny] = 7
                    elif O[nx][ny] == 6:
                        break
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not O[i][j]:
                    cnt += 1
        ans = min(ans, cnt)
        return
    x, y, c = CCTV[len(Direction)]
    for n in range(len(D[c])):
        Direction.append((x,y,c,n))
        dfs(Direction)
        Direction.pop()
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
I = sys.stdin.readline
N, M = map(int, I().split())
Office = [list(map(int,I().split())) for _ in range(N)]
d = (0,-1),(-1,0),(0,1),(1,0)
D = (0,
    ((0,), (1,), (2,), (3,)),
    ((0,2), (1,3)),
    ((0,1), (1,2), (2,3), (0,3)),
    ((0,1,2), (1,2,3), (0,2,3), (0,1,3)),
    ((0,1,2,3),)
    )
CCTV = deque()
for x in range(N):
    for y in range(M):
        if 0<Office[x][y]<6:
            CCTV.append((x,y,Office[x][y]))
Direction = deque()
ans = 64
dfs(Direction)
print(ans)
```