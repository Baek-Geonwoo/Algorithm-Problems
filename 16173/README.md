# 백준 16173번 점프왕 쩰리 (Small)
https://www.acmicpc.net/problem/16173
---

### 문제 해결 날짜
- 2021.02.14
---

### 코드 설명
- ```M[x][y]에 도착하면 오른쪽으로 M[x][y]칸 또는 아래쪽으로 M[x][y]칸 움직일 수 있다.```
- stack을 통해 DFS를 구현했다.
- ```M[x][y]에서 움직여 도착한 칸이 N*N 정사각형 범위 안인지 확인한 후, 방문한 칸인지 확인하여 방문하지 않았으면 stack에 해당 칸을 추가하고 visited를 업데이트한다.```
- while루프에서 매번 ```visited[N-1][N-1]이 방문되었는지 확인하고 방문되었다면 True를 리턴하고, while루프가 끝나면 M[N-1][N-1]이 방문되지 않았다는 것이므로 False를 리턴한다.```
---

### 소스코드
- 메모리 : 32404KB
- 시간 : 88ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def DFS(x,y):
    visited = [[False]*N for _ in range(N)]
    m = M[x][y]
    Q = deque([[x,y]])
    while Q:
        if visited[N-1][N-1]:
            return True
        x, y = Q.pop()
        m = M[x][y]
        for i in range(2):
            X, Y = x+m*dx[i], y+m*dy[i]
            if 0<=X<N and 0<=Y<N:
                if not visited[X][Y]:
                    Q.append([X,Y])
                    visited[X][Y] = True
    return False

N = int(I())
M = [list(map(int,I().split())) for _ in range(N)]
dx = [0,1]
dy = [1,0]
if DFS(0,0):
    print("HaruHaru")
else:
    print("Hing")
```
---
### 오답노트
- 백트래킹 문제라서 백트래킹으로 풀었더니 시간복잡도가 O(4^N)이 나와서 시간초과가 떴다.

### 오답코드
```Python
import sys
def solution(i):
    global N, ans
    if i == N:
        S.add(ans)
        return
    for r in R:
        ans += r
        solution(i+1)
        ans -= r
N = int(sys.stdin.readline())
S = set()
R = [1, 5, 10, 50]
ans = 0
solution(0)
print(len(S))
```