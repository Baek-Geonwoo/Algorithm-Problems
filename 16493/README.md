# 백준 16493번 최대 페이지 수
https://www.acmicpc.net/problem/16493
---

### 문제 해결 날짜
- 2022.04.17
---

### 코드 설명
- ```dp[m][n]은 m번째 챕터 까지 n일 동안 읽을 수 있을 때 읽을 수 있는 최대 페이지 수이다.```
- ```A[m][0] <= n``` 즉, n번째 챕터를 읽을 수 있는 경우
    * ```dp[m][n] = max(A[m][1] + dp[m-1][n-A[m][0]], dp[m-1][n])```
- ```A[m][0] > n``` n번째 챕터를 읽을 수 없는 경우
    * ```dp[m][n] = dp[m-1][n]```
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
N, M = map(int, I().split())
A = [0]+[tuple(map(int, I().split())) for _ in range(M)]
# dp[m][n]은 m번째 챕터 까지 n일 동안 읽을 수 있을 때 읽을 수 있는 최대 페이지 수
dp = [[0]*(N+1) for _ in range(M+1)]
for m in range(1,M+1):
    for n in range(1,N+1):
        if A[m][0] <= n:
            dp[m][n] = max(A[m][1] + dp[m-1][n-A[m][0]], dp[m-1][n])
        else:
            dp[m][n] = dp[m-1][n]
print(dp[M][N])
```