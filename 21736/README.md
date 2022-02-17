# 백준 21736번 헌내기는 친구가 필요해
https://www.acmicpc.net/problem/21736
---

### 문제 해결 날짜
- 2021.02.17
---

### 코드 설명
- I를 C에서 찾아서 그 위치를 stack에 저장한다.
- stack이 빌 때까지 DFS로 C를 탐색하여 방문가능한 P의 수를 모두 구한다.
    * ```C[x][y]가 X라면 continue로 건너뛴다.```
    * ```C[x][y]가 O 또는 P라면 stack에 x,y의 NxM범위 내의 상하좌우위치를 추가하고, P면 ans+=1한다.```
---

### 소스코드
- 메모리 : 123948KB
- 시간 : 1392ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
C = [I().strip() for _ in range(N)]
stack = deque()
for i in range(N):
    for j in range(M):
        if C[i][j] == 'I':
            stack.append((i,j))
visited = [[False]*M for _ in range(N)]
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while stack:
    x, y = stack.pop()
    if not visited[x][y]:
        visited[x][y] = True
        if C[x][y] == 'X':
            continue
        if C[x][y] == 'P':
            ans += 1
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if in_range(X,Y):
                stack.append((X,Y))
if not ans:
    print("TT")
else:
    print(ans)
```