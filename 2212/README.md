# 백준 2212번 센서
https://www.acmicpc.net/problem/2212
---

### 문제 해결 날짜
- 2022.05.22
---

### 코드 설명
- 센서 사이의 거리들 중 가장 큰 K-1개의 간격만큼을 전체 범위에서 빼면 된다.
- A를 정렬하고 min-heap에 센서간의 간격의 크기들을 넣고 크기를 K-1 이하로 유지한다.
- 전체 범위(`A[-1] - A[0]`)에서 가장 큰 간격 K-1개의 합(sum(H))를 뺀다.
---

### 소스코드
- 메모리 : 32908 KB
- 시간 : 84 ms
```Python
import sys
from heapq import heappush, heappop
N, K, *A = map(int, sys.stdin.read().split())
H = []
A.sort()
for i in range(N-1):
    if len(H) < K-1:
        heappush(H, A[i+1]-A[i])
    else:
        heappush(H, A[i+1]-A[i])
        heappop(H)
print(A[-1] - A[0] - sum(H))
```