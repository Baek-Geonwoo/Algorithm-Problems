# 백준 11286번 절댓값 힙
https://www.acmicpc.net/problem/11286
---

### 문제 해결 날짜
- 2022.04.09
---

### 코드 설명
- 힙에 (절댓값, 값)인 튜플을 저장하여 절댓값, 값 순으로(절댓값이 같으면 값이 작은 것이 위로) 힙을 구성한다.
---

### 소스코드
- 메모리 : 39052KB
- 시간 : 172ms
```Python
import sys
import heapq
I = sys.stdin.readline
N = int(I())
H = []
for _ in range(N):
    a = int(I())
    if a == 0:
        if H:
            print(heapq.heappop(H)[1])
        else:
            print(0)
    else:
        heapq.heappush(H,(abs(a),a))
```