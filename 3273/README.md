# 백준 3273번 두 수의 합
https://www.acmicpc.net/problem/3273
---

### 문제 해결 날짜
- 2021.03.23
---

### 코드 설명
- A를 정렬하여 L, R로 L < R인 동안 A를 순회한다.
- ```S = A[L] + A[R]라 하여 S == x 이면 ans += 1```
- S < x 이면 L += 1
- S >= x 이면 R += 1
---

### 소스코드
- 메모리 : 41892KB
- 시간 : 116ms
```Python
import sys
N, *A, x = map(int, sys.stdin.read().split())
A.sort()
L, R = 0, N-1
ans = 0
while L < R:
    S = A[L] + A[R]
    if S == x: ans += 1
    if S < x: L += 1
    else: R -= 1
print(ans)
```