# 백준 2583번 영역 구하기
https://www.acmicpc.net/problem/2583
---

### 문제 해결 날짜
- 2021.02.18
---

### 코드 설명
- 모눈종이에서 각 칸을 이루는 사각형의 왼쪽 아래의 점을 그 사각형으로 간주한다.
    * 예를 들어 0 0 1 1인 사각형은 0 0인 점을 그 사각형으로 간주한다.
- 각 직사각형들이 차지하는 점들을 visited에서 True로 초기화하여 DFS를 할 때 방문하지 않도록 한다.
- ```N*M 범위에서 각 점에서(그 점이 방문되지 않았다면) DFS를 하여 한번의 DFS당 방문한 점의 수가 곧 영역의 넓이이므로 이를 A에 append한다.```
---

### 소스코드
- 메모리 : 32444KB
- 시간 : 112ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<M and 0<=y<N:
        return True
    return False
M, N, K = map(int, I().split())
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    b,a,d,c = map(int,I().split())
    for i in range(a,c):
        for j in range(b,d):
            visited[i][j] = 1
A = []
dx = (-1,1,0,0)
dy = (0,0,-1,1)
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            ans = 0
            stack = deque()
            stack.append((i,j))
            while stack:
                x, y = stack.pop()
                visited[x][y] = 1
                ans += 1
                for k in range(4):
                    X = x+dx[k]
                    Y = y+dy[k]
                    if in_range(X,Y) and not visited[X][Y]:
                        stack.append((X,Y))
                        visited[X][Y] = 1
            A.append(ans)
A.sort()
print(len(A))
for a in A:
    print(a, end=" ")
```
---
### 오답노트
- i, j로 루프를 도는데 그 안에서 i를 반복자로 루프를 또다시 돌아서 문제가 발생했다.

### 오답코드
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<M and 0<=y<N:
        return True
    return False
M, N, K = map(int, I().split())
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    b,a,d,c = map(int,I().split())
    for i in range(a,c):
        for j in range(b,d):
            visited[i][j] = 1
A = []
dx = (-1,1,0,0)
dy = (0,0,-1,1)
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            ans = 0
            stack = deque()
            stack.append((i,j))
            while stack:
                x, y = stack.pop()
                visited[x][y] = 1
                ans += 1
                for i in range(4):
                    X = x+dx[i]
                    Y = y+dy[i]
                    if in_range(X,Y) and not visited[X][Y]:
                        stack.append((X,Y))
                        visited[X][Y] = 1
            A.append(ans)
A.sort()
print(len(A))
for a in A:
    print(a, end=" ")
```