# 백준 1715번 카드 정렬하기
https://www.acmicpc.net/problem/1715
---

### 문제 해결 날짜
- 2022.04.07
---

### 코드 설명
- 크기가 작은 묶음들부터 하나로 합쳐야 비교횟수가 가장 적다.
- 두 카드 묶음을 합칠 때마다 묶음이 1개 줄어드는 것이므로 다음을 N-1번 반복한다.
- 카드 묶음의 크기들을 heap에 넣고 heappop을 통해 가장 작은 두 묶음을 합치고(이 값이 compare에 저장됨) 비교횟수(두 덱의 크기의 합)을 ans에 더하고, compare을 heap에 추가한다.
---

### 소스코드
- 메모리 : 39616KB
- 시간 : 196ms
```Python
import sys, heapq
N, *heap = map(int, sys.stdin.read().split())
heapq.heapify(heap)
ans = 0
for _ in range(N-1):
    compare = heapq.heappop(heap) + heapq.heappop(heap)
    ans += compare
    heapq.heappush(heap, compare)
print(ans)
```