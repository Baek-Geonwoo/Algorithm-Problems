# 백준 1916번 최소비용 구하기
https://www.acmicpc.net/problem/1916
---

### 문제 해결 날짜
- 2022.06.15
---

## 풀이 1 - 다익스트라(그래프를 리스트로 구현)

### 코드 설명
- 그래프를 리스트로 구현했다. 거리 dp테이블의 초기값은 fare가 100000이하이고, 최악의 경우 N-1번 버스를 타야하므로 `100000*N`으로 설정했다.
- (현재 위치까지 오는 데 드는 비용, 현재 위치) 쌍을 heap에서 pop하여 `graph[현재위치]`를 순회하며 distance가 업데이트되면 (버스 종착지점, 현재위치까지의 비용+버스비용) 쌍을 heap에 push한다.
---

### 소스코드
- 메모리 : 55632 KB
- 시간 : 352 ms
```Python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, fare = map(int, input().split())
    graph[start].append((fare, end))
distance = [0] + [100000*N]*N
start, end = map(int, input().split())
H = [(0, start)]
while H:
    fare, curr = heappop(H)
    if distance[curr] >= fare:
        for f, e in graph[curr]:
            if distance[e] > f + fare:
                distance[e] = f + fare
                heappush(H, (distance[e], e))
print(distance[end])
```
---
## 풀이 2 - 다익스트라(그래프를 리스트와 딕셔너리를 섞어서 구현)

### 코드 설명
- 1번과 비슷하지만 그래프를 리스트로 구현하면 사용하지 않는 부분이 생길 수 있어서 2차원은 리스트로, 1차원은 딕셔너리로 그래프를 구현했다.
---

### 소스코드
- 메모리 : 37720 KB
- 시간 : 220 ms
```Python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [dict() for _ in range(N+1)]
for _ in range(M):
    start, end, fare = map(int, input().split())
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], fare)
    else:
        graph[start][end] = fare
distance = [0] + [100000*N]*N
start, end = map(int, input().split())
H = [(0, start)]
while H:
    fare, curr = heappop(H)
    if distance[curr] >= fare:
        for e, f in graph[curr].items():
            if distance[e] > f + fare:
                distance[e] = f + fare
                heappush(H, (distance[e], e))
print(distance[end])
```
---
## 풀이 2 - 다익스트라(그래프와 거리저장 모두 딕셔너리 사용)

### 코드 설명
- 2번과 비슷하지만 그래프를 2차원 딕셔너리로, 거리 저장 dp테이블도 딕셔너리로 구현했다.
---

### 소스코드
- 메모리 : 37704 KB
- 시간 : 256 ms
```Python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = {}
distance = {}
for _ in range(M):
    start, end, fare = map(int, input().split())
    if start not in graph:
        graph[start] = {}
    if start not in distance:
        distance[start] = 100000*N
    if end not in distance:
        distance[end] = 100000*N
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], fare)
    else:
        graph[start][end] = fare

start, end = map(int, input().split())
H = [(0, start)]
while H:
    fare, curr = heappop(H)
    if distance[curr] >= fare and curr in graph:
        for e, f in graph[curr].items():
            if distance[e] > f + fare:
                distance[e] = f + fare
                heappush(H, (distance[e], e))
print(distance[end])
```
---

## 느낀점
- 딕셔너리로 그래프나 dp테이블을 구현하면 사용하지 않는 공간이 선언되는 일이 줄어들어 시간과 메모리 모두에서 이득을 볼 것이라고 예상했고, 그래프를 2차원은 리스트, 1차원은 딕셔너리로 구현했을 때에는 예상대로 되었지만 그래프를 2차원 딕셔너리로 구현하니 메모리에서는 이득을 보았지만 시간에서 손해를 보았다.
- 자료구조의 특성에 맞게 적당히 선택하여 사용해야 한다는 것을 배웠다.