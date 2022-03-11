# 백준 2225번 합분해
https://www.acmicpc.net/problem/2225
---

### 문제 해결 날짜
- 2021.03.11
---

### 코드 설명
- ```P[i]는 k개의 정수의 합으로 i를 나타낼 수 있는 경우의 수이다.```
- ```dp[k][i]를 k개의 정수로 i를 만드는 경우의 수라 하면 다음과 같다.```
    * ```dp[k][i] = dp[k-1][i] + dp[k-1][i-1] ... dp[k-1][0]```
    * ```dp[k][i-1] = dp[k-1][i-1] ... dp[k-1][0]```
    * 따라서 ```dp[k][i] = dp[k-1][i] + dp[k][i-1]```가 성립한다.
- 그러므로 ```P[i] = (P[i] + P[i-1])%1000000000이다.```
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 80ms
```Python
import sys
N, K = map(int, sys.stdin.readline().split())
P = [0]*(N+1)
P[0] = 1
for k in range(1,K+1):
    for i in range(1,N+1):
        P[i] = (P[i] + P[i-1])%1000000000
print(P[N])
```

---
### 오답노트
- DFS로 풀었는데 그러다보니 시간복잡도가 O(N^K)가 되어 시간초과가 발생했다.

### 오답코드
```Python
import sys
def dfs(k,n):
    if k == K:
        if n <= N:
            P[k][n] = (P[k][n]+1)%1000000000
        return
    if n > N:
        return
    for i in range(N+1):
        dfs(k+1,n+i)
N, K = map(int, sys.stdin.readline().split())
P = [[0]*(N+1) for _ in range(K+1)]
dfs(0,0)
print(P[K][N])
```