# 백준 1443번 망가진 계산기
https://www.acmicpc.net/problem/1443
---

### 문제 해결 날짜
- 2021.02.27
---

### 코드 설명
- S에 (현재 계산기에 적힌 수, 곱셈횟수)들을 저장한다.
- D 자리수 이하의 수들을 10^D 미만의 수들이므로 D를 10^D로 초기화한다.
- 문제의 수를 구하는 과정에서 n이 D 이상이거나 (n,i)가 이미 S에 있는 경우 중복이므로 재귀를 중단한다.
---

### 소스코드
- 메모리 : 34448KB
- 시간 : 116ms
```Python
import sys
def broken_calc(n,i):
    global D, P, ans
    if n >= D:
        return
    if (n,i) in S:
        return
    S.add((n,i))
    if i == P:
        if n < D:
            ans = max(ans, n)
        return
    for x in range(2,10):
        broken_calc(n*x,i+1)
D, P = map(int, sys.stdin.readline().split())
D = 10**D
ans = 0
S = set()
broken_calc(1,0)
print(ans) if ans != 0 else print(-1)
```
---
### 오답노트
- 중복체크를 하지 않아 시간초과가 발생했다.

### 오답코드
```Python
import sys
def broken_calc(n,i):
    global D, P, ans
    if i == P:
        if n <= D:
            ans = max(ans, n)
        return
    for x in range(2,10):
        broken_calc(n*x,i+1)
D, P = map(int, sys.stdin.readline().split())
D = int("9"*D)
ans = 0
broken_calc(1,0)
print(ans) if ans != 0 else print(-1)
```