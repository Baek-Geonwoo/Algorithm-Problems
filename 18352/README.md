# 백준 18352번 특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352
---

### 문제 해결 날짜
- 2021.02.23
---

### 코드 설명
- ```D[v]에는 X에서 v까지 가는 최소 거리가 저장된다.```
- ```G[v]에는 v에서 갈 수 있는 도시들이 저장된다.```
- X부터 G를 BFS로 순회하며 X에서 갈 수 있는 도시들 까지의 최단 거리들을 D에 업데이트한다. ```D[v]가 -1이면 방문한 적이 없다는 것이고, 가중치가 1로 동일하므로 BFS 특성상 깊이가 깊어질수록 거리가 늘어난다. 즉, 첫 방문이 가장 최소 거리이다. 따라서 D[v]가 `1일때만(방문한 적이 없는 도시일 때) D[u]+1로 초기화해준다.```
- D를 순회하며 ```D[v]가 K인 모든 v를 출력한다.(이때 v가 1부터 N까지 순회하므로 출력되는 v는 오름차순이다.```
- 만약 ```D[v]가 K인 v가 없다면 -을 출력한다.```
---

### 소스코드
- 메모리 : 98352KB
- 시간 : 2004ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
N, M, K, X = map(int,I().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, I().split())
    G[A].append(B)
D = [-1]*(N+1)
D[X] = 0
Q = deque((X,))
while Q:
    u = Q.popleft()
    for v in G[u]:
        if D[v] == -1:
            D[v] = D[u]+1
            Q.append(v)
cnt = 0
for i in range(1,N+1):
    if D[i] == K:
        print(i)
        cnt += 1
if not cnt:
    print(-1)
```
---
### 오답노트
- 첫 방문이 가장 최소거리인데 그것을 나중에 알아서 같은 도시에 대해서 계속 탐색을 하다 보니 시간초과가 발생했다.

### 오답코드
```Python
import sys
from collections import deque
I = sys.stdin.readline
N, M, K, X = map(int,I().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, I().split())
    G[A].append(B)
D = [N]*(N+1)
D[X] = 0
Q = deque(((X,0),))
while Q:
    u, d = Q.pop()
    D[u] = min(D[u],d)
    for v in G[u]:
        Q.appendleft((v,d+1))
cnt = 0
for i in range(1,N+1):
    if D[i] == K:
        print(i)
        cnt += 1
if not cnt:
    print(-1)
```