# 백준 2108번 통계학
https://www.acmicpc.net/problem/2108
---

### 문제 해결 날짜
- 2021.03.22
---

### 코드 설명
- 산술평균, 중앙값을 구하고, 최빈값은 Counter를 사용해서 구헸다. 범위는 N이 1이면 존재하지 않으므로 0이다.
---

### 소스코드
- 메모리 : 89900KB
- 시간 : 400ms
```Python
import sys
from collections import Counter
N, *A = map(int, sys.stdin.read().split())
A.sort()
print(round(sum(A)/N))
print(A[N//2])
C = Counter(A).most_common()
if N > 1:
    if C[0][1] == C[1][1]:
        print(C[1][0])
    else:
        print(C[0][0])
    print(A[-1]-A[0])
else:
    print(A[0])
    print(0)
```