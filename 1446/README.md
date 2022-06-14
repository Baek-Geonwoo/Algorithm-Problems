# 백준 1446번 지름길
https://www.acmicpc.net/problem/1446
---

### 문제 해결 날짜
- 2022.06.15
---

## 풀이 1 - 브루트포스

### 코드 설명
- D가 10000 이하의 자연수이고 N이 12 이하의 자연수이므로 시간복잡도가 O(ND)여도 시간초과가 발생하지 않는다.
- 딕셔너리로 그래프를 형성하고 dict.get을 사용해 KeyError를 방지한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 68 ms
```Python
import sys
input = sys.stdin.readline
N, D = map(int, input().split())
distance = [0]*(D+1)
shortcut = {}

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        if shortcut.get(e) == None:
            shortcut[e] = []
        shortcut[e].append((s,d))

for i in range(1,D+1):
    distance[i] = distance[i-1]+1
    if shortcut.get(i) != None:
        for s, d in shortcut[i]:
            distance[i] = min(distance[i], distance[s]+d)
print(distance[D])
```
---
## 풀이 2 - heap

### 코드 설명
- 그래프를 리스트로 형성하는데 `0~D-1`는 바로 다음위치로 1의 거리를 이동해 갈 수 있으므로 그래프를 `graph = [[(i+1,1)] for i in range(D)]+[[]]`로 초기화한다.
- `distance[지름길 도착지점] < 현재위치까지의 최단거리 + 지름길 길이`이면 (현재위치까지의 최단거리 + 지름길 길이, 지름길 도착지점)를 heap에 update하며 heap이 빌 때까지 이를 반복한다.
---

### 소스코드
- 메모리 : 32908 KB
- 시간 : 72 ms
```Python
import sys
from heapq import *
input = sys.stdin.readline
N, D = map(int, input().split())
graph = [[(i+1,1)] for i in range(D)]+[[]]

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        graph[s].append((e,d))

distance = [D]*(D+1)
H = []
heappush(H, (0,0))
while H:
    d, pos = heappop(H)
    if distance[pos] >= d:
        for end, length in graph[pos]:
            dist = d + length
            if distance[end] > dist:
                distance[end] = dist
                heappush(H, (dist, end))
print(distance[D])
```