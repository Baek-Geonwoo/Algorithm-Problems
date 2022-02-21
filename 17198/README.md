# 백준 17198번 Bucket Brigade
https://www.acmicpc.net/problem/17198
---

### 문제 해결 날짜
- 2021.02.21
---

### 코드 설명
- Q안에 들어가는 x, y, p는 각각 ```F[x][y], p(path, 경로길이)이다.(p는 L에서 F[x][y]까지 이동한 경로의 길이)```
- ```F[x][y] == 'B'거나 Q가 비면 while 루프가 종료된다.(문제상 B에 도달하지 못하는 경우는 없으므로 Q가 비어서 종료되는 경우는 사실상 없다.)```
- 정답은 ```F[x][y] == 'B'일 때 p-1이다. p는 L에서 B까지의 최단거리의 길이인데 문제에서 구하는 것은 배치해야 하는 소의 최소 수이기 때문이다.```
---

### 소스코드
- 메모리 : 32412KB
- 시간 : 92ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
def in_range(x,y):
    if 0<=x<10 and 0<=y<10:
        return True
    return False
F = [I().strip() for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
d = ((-1,0),(1,0),(0,-1),(0,1))
Q = deque()
for i in range(10):
    for j in range(10):
        if F[i][j] == 'R':
            visited[i][j] = 1
        elif F[i][j] == 'L':
            L = i,j,0
Q.appendleft(L)
while Q:
    x, y, p = Q.pop()
    if F[x][y] == 'B':
        print(p-1)
        break
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if in_range(nx,ny) and not visited[nx][ny]:
            visited[nx][ny] = 1
            Q.appendleft((nx,ny,p+1))
```