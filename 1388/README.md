# 백준 1388번 바닥 장식
https://www.acmicpc.net/problem/23559
---

### 문제 해결 날짜
- 2021.02.15
---

### 풀이1 코드 설명
- DFS를 통해 아래, 오른쪽 순으로 F(바닥 장식)을 탐색한다.
- visited에 해당 칸의 방문여부를 저정하고 Q가 빌 때까지 방문하지 않은 칸에 대해서 해당 칸의 아래, 오른쪽 칸에서 다음을 시행한다.
    * ```F[X][Y]가 '-'라면 그 왼쪽, F[X][Y-1]이 가능한 위치가 아니거나 '|'일 경우 다른 판자이므로 ans+=1```
    * ```F[X][Y]가 '|'라면 그 위쪽, F[X-1][Y]이 가능한 위치가 아니거나 '-'일 경우 다른 판자이므로 ans+=1```
---

### 풀이1 소스코드
- 메모리 : 32420KB
- 시간 : 96ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
F = [list(I().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0,1]
dy = [1,0]
Q = deque([[0,0]])
visited[0][0] = True
ans = 1
while Q:
    x, y = Q.pop()
    for i in range(2):
        X = x+dx[i]
        Y = y+dy[i]
        if in_range(X,Y):
            if not visited[X][Y]:
                Q.append([X,Y])
                visited[X][Y] = True
                i = X-int(F[X][Y]=='|')
                j = Y-int(F[X][Y]=='-')
                if in_range(i,j):
                    if F[X][Y] != F[i][j]:
                        ans += 1
                else:
                    ans += 1
print(ans)
```
---

### 풀이2 코드 설명
- x에 대해서 range(N), y에 대해서 range(M)의 순회를 하면서 모든 ```F[x][y]```에 대해서 다음을 실행한다.
    * ```F[x][y]가 '-'라면 그 왼쪽, F[x][y-1]이 가능한 위치가 아니거나 '|'일 경우 다른 판자이므로 ans+=1```
    * ```F[x][y]가 '|'라면 그 위쪽, F[x-1][y]이 가능한 위치가 아니거나 '-'일 경우 다른 판자이므로 ans+=1```
---

### 풀이2 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
N, M = map(int, I().split())
F = [list(I().strip()) for _ in range(N)]
ans = 0
for x in range(N):
    for y in range(M):
        X = x-int(F[x][y]=='|')
        Y = y-int(F[x][y]=='-')
        if in_range(X,Y):
            if F[x][y] != F[X][Y]:
                ans += 1
        else:
            ans += 1
print(ans)
```
---
### 느낀점
- DFS 문제지만 단순 순회를 통해서 푼 방법이 더 시간이 적게 걸렸다. 앞으로도 여러가지 방법으로 문제를 해결해 보아야겠다.