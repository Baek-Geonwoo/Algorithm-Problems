# 백준 1753번 최단경로
https://www.acmicpc.net/problem/1753
---

### 문제 해결 날짜
- 2022.06.02
---

### 코드 설명
- u -w-> v이면 `G[u].append((w,v))`하여 그래프를 구성한다.
- 시작점의 최단경로 값은 0이고, `distance[v] > n_w + w`이면 heap에 (시작점부터 현재까지의 최단경로 값, 다음 정점)을 저장하며 heap이 빌 떄까지 이 과정을 반복한다.
---

### 소스코드
- 메모리 : 66916 KB
- 시간 : 744 ms
```Python
import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')
V, E = map(int, input().split())
K = int(input())
G = [0] + [[] for _ in range(V)]
distance = [0] + [INF]*V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((w,v))
map(list.sort, G)
distance[K] = 0
H = []
heappush(H, (0,K))
while H:
    w, u = heappop(H)
    if distance[u] < w:
        continue
    for n_w, v in G[u]:
        if distance[v] > n_w + w:
            distance[v] = n_w + w
            heappush(H, (n_w + w,v))
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```