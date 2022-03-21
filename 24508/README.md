# 백준 24508번 나도리팡
https://www.acmicpc.net/problem/24508
---

### 문제 해결 날짜
- 2021.03.21
---

### 코드 설명
- s, e는 ```A[s]에서 A[e]로 옮긴다.```
- ```A[s] < K-A[e]이면 A[s]의 나도리를 A[e]로 모두 옮길 수 있는 경우이다.```
- ```A[s] == K-A[e]이면 A[s]의 나도리를 A[e]로 모두 옮겼을 때 A[e]의 나도리가 터지는 경우이다.```
- ```A[s] > K-A[e]이면 A[s]의 나도리 일부를 A[e]로 옮겼을 때 A[e]의 나도리가 터지는 경우이다.```
- 나도리를 옮길 때마다 ```A[s], A[e], cnt를 업테이트한다.```
- cnt(옮긴 나도리의 수) < T, s < e인 동안 위 과정을 반복하며 반복이 끝났을 때 cnt <= T 이고 sum(A) == 0(모든 나도리가 터짐)이면 나도리를 T회 이하로 옮겨 모두 터트릴 수 있다.
---

### 소스코드
- 메모리 : 42028KB
- 시간 : 196ms
```Python
import sys
N, K, T, *A = map(int, sys.stdin.read().split())
A.sort()
s, e = 0, N-1; cnt = 0
while s < e and cnt < T:
    if A[s] < K-A[e]:
        A[e] += A[s]
        cnt += A[s]
        A[s] = 0
        s += 1
    elif A[s] == K-A[e]:
        A[e] += A[s]
        cnt += A[s]
        A[s] = 0
        s += 1
        A[e] = 0
        e -= 1
    else:
        A[s] -= K-A[e]
        cnt += K-A[e]
        A[e] = 0
        e -= 1
print("YES") if cnt <= T and sum(A)==0 else print("NO")
```
---
### 오답노트
- 시간복잡도가 O(T)인데 T가 최악의 경우 10^9이라 시간초과가 발생했다.

### 오답코드
```Python
import sys
from collections import deque
N, K, T, *A = map(int, sys.stdin.read().split())
A = deque(sorted(A))
cnt = 0
while len(A) > 1 and cnt < T:
    A[0] -= 1; A[-1] += 1
    if A[0] == 0:
        A.popleft()
    if A[-1] == K:
        A.pop()
    cnt += 1
print("NO") if A else print("YES")
```