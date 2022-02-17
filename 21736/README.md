# 백준 21736번 헌내기는 친구가 필요해
https://www.acmicpc.net/problem/21736
---

### 문제 해결 날짜
- 2021.02.17
---

### 코드 설명
- I를 C에서 찾아서 그 위치를 stack에 저장한다.
- stack이 빌 때까지 DFS로 C를 탐색하여 방문가능한 P의 수를 모두 구한다.
    * ```C[x][y]가 X가 아니라면 stack에 x,y의 NxM범위 내의 방문하지 않은 상하좌우위치를 추가하고, P면 ans+=1한다.```
---

### 소스코드
- 메모리 : 50744KB
- 시간 : 980ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
N, M = map(int, I().split())
C = [I().strip() for _ in range(N)]
stack = deque()
for i in range(N):
    for j in range(M):
        if C[i][j] == 'I':
            stack.append((i,j))
            break
visited = [[0]*M for _ in range(N)]
ans = 0
dx = (-1,1,0,0)
dy = (0,0,-1,1)
while stack:
    x, y = stack.pop()
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0<=X<N and 0<=Y<M and not visited[X][Y]:
            if C[X][Y] != 'X':
                if C[X][Y] == 'P':
                    ans += 1
                visited[X][Y] = 1
                stack.append((X,Y))
print(ans) if ans else print("TT")
```