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
- 메모리 : KB
- 시간 : ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<M and 0<=y<N:
        return True
    return False
M, N, K = map(int, I().split())
visited = [[False]*N for _ in range(M)]
for _ in range(K):
    b,a,d,c = map(int,I().split())
    for i in range(a,c):
        for j in range(b,d):
            visited[i][j] = True
A = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(M):
    for j in range(N):
        ans = 0
        if not visited[i][j]:
            stack = deque([[i,j]])
            while stack:
                x, y = stack.pop()
                if not visited[x][y]:
                    visited[x][y] = True
                    ans += 1
                    for i in range(4):
                        X = x+dx[i]
                        Y = y+dy[i]
                        if in_range(X,Y):
                            stack.append([X,Y])
            A.append(ans)
A.sort()
print(len(A))
for a in A:
    print(a, end=" ")
```