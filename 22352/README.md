# 백준 22352번 항체 인식
https://www.acmicpc.net/problem/22352
---

### 문제 해결 날짜
- 2022.05.26
---

### 접근 방식
- 백신 투약 전의 촬영결과를 A에 백신 투약 후의 촬영결과를 B에 저장한다.
- A를 BFS로 탐색하며 항체가 퍼져나갈 수 있는 곳들을 하나의 리스트로 하여 S에 저장한다.
- S를 순회하며 B에서 A의 값과 다르면 kind에 해당 값을 표시한다.
    * kind 크기가 0이면 변화가 없거나 변화가 있지만 우연히 데이터가 전과 같은 것이므로 continue
    * kind의 크기가 2이상이거나 kind의 값이 구역의 크기와 다르면 같은 구역에 서로 다른 데이터값이 2개이상인 것이므로 답은 NO가 된다.
    * kind의 크기가 1이면 cnt를 1 증가시킨다.
- 항체가 퍼져나갈 수 있는 곳은 한 구간이므로 cnt가 1이하이면 YES 아니면 NO이다.
---

### 소스코드
- 메모리 : 32540 KB
- 시간 : 92 ms
```Python
import sys
from collections import deque, defaultdict
d = (-1,0), (1,0), (0,-1), (0,1)
def input():
    return [int(e) for e in sys.stdin.readline().split()]
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
def bfs(n,x,y):
    V = [(x,y)]
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    while Q:
        x, y = Q.pop()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and A[nx][ny] == n:
                Q.appendleft((nx, ny))
                V.append((nx,ny))
                visited[nx][ny] = 1
    return V
N, M = input()
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
S = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            S.append(bfs(A[i][j],i,j))
cnt = 0
for s in S:
    x, y = s[0]
    n = A[x][y]
    kind = defaultdict(int)
    for x,y in s:
        if B[x][y] != n:
            kind[B[x][y]] += 1
    if len(kind) == 0:
        continue
    elif len(kind) >= 2 or kind[B[x][y]] != len(s):
        cnt = 2
        break
    elif len(kind) == 1:
        cnt += 1
if cnt <= 1:
    print('YES')
else:
    print('NO')
```