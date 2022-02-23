# 백준 18232번 텔레포트 정거장
https://www.acmicpc.net/problem/18232
---

### 문제 해결 날짜
- 2021.02.24
---

### 코드 설명
- ans에 S부터 E까지 갈 수 있는 최소시간을 저장한다.(초기값은 abs(S-E)이다. S부터 E까지 1칸씩 이동한 경우가 ans에 들어갈 수 있는 최댓값이기 때문이다.)
- ```x-y로 연결되어 있으므로 T[x].append(y), T[y].append(x)하여 텔레포트 연결을 T에 저장한다.```
- X는 현재위치이고, t는 X까지 이동하는 데 필요한 시간이다.
- Q가 빌 때까지 다음을 반복한다.
    * X==E이면 ans = min(ans,t)로 초기화하고 continue한다.
    * ```T[X]가 비어있지 않다면, 텔레포트가 가능하므로 T[X]를 i로 순회하며 i가 방문되지 않았다면 Q에 (i,t+1)을 추가한다.```
    * X에서 ```i in [-1,1]로 X+i가 방문되지 않았다면 Q에 (X+i,t+1)을 추가한다.``` 
---

### 소스코드
- 메모리 : 92116KB
- 시간 : 1380ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
N, M = map(int, I().split())
S, E = map(int, I().split())
T = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, I().split())
    T[x].append(y)
    T[y].append(x)
Q = deque(((S,0),))
visited = [0]*(N+1)
visited[S] = 1
ans = abs(S-E)
while Q:
    X, t = Q.pop()
    if X == E:
        ans = min(ans, t)
        continue
    if T[X]:
        for i in T[X]:
            if not visited[i]:
                Q.appendleft((i,t+1))
                visited[i] = 1
    for d in range(-1,2,2):
        if 1<=X+d<=N and not visited[X+d]:
            Q.appendleft((X+d,t+1))
            visited[X+d] = 1
print(ans)
```