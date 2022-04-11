# 백준 1351번 무한 수열
https://www.acmicpc.net/problem/1351
---

### 문제 해결 날짜
- 2022.04.11
---

### 코드 설명
- ```A[0] = 1```
- ```A[i] = A[i/P] + A[i/Q]```
- 중복으로 구해지는 ```A[i]```가 없도록 defaultdict를 사용한다.
    * 리스트로 dp테이블을 구현하기에는 N이 최대 10^12이라 시간초과가 발생한다.
- 따라서 DFS를 통해 ```A[N]```을 구한다.
---

### 소스코드
- 메모리 : 32424KB
- 시간 : 88ms
```Python
import sys
from collections import defaultdict
def dfs(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = dfs(n//P)+dfs(n//Q)
    return dp[n]
N, P, Q = map(int, sys.stdin.readline().split())
dp = defaultdict(int)
dp[0] = 1
print(dfs(N))
```
---

### 오답 노트
- 시간 초과
- ```A[i]```를 이미 구했음에도 중복으로 다시 구하는 방식이라 시간초과가 발생했다.

### 오답 코드
```Python
import sys
def dfs(n):
    if n == 0:
        return 1
    return dfs(n//P)+dfs(n//Q)
N, P, Q = map(int, sys.stdin.readline().split())
print(dfs(N))
```