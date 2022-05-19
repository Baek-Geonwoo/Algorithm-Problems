# 백준 23843번 콘센트
https://www.acmicpc.net/problem/23843
---

### 문제 해결 날짜
- 2022.05.19
---

### 코드 설명
- 콘센트 개수 M 만큼의 크기를 가진 충전기를 최소힙으로 한다.
- 충전기에 시간이 오래걸리는 전자기기부터 충전한다.
- 충전기 콘센트가 다 차면 pop한후 t를 더해서 push한다.
- 충전기에서 가장 오래걸리는 콘센트를 찾는다.(그 시간이 충전에 필요한 최소 시간이다.)
---

### 소스코드
- 메모리 : 32908 KB
- 시간 : 80 ms
```Python
import sys
from heapq import *
input = sys.stdin.readline

N, M = map(int, input().split())
T = sorted(list(map(int, input().split())),reverse=True)
charger = []
for t in T:
    if len(charger) < M:
        heappush(charger, t)
    else:
        heappush(charger, heappop(charger)+t)
print(max(charger))
```