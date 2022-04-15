# 백준 22115번 창영이와 커피
https://www.acmicpc.net/problem/22115
---

### 문제 해결 날짜
- 2022.04.15
---

## 풀이 1 - DP(2차원)

### 코드 설명
- ```dp[k][n]은 n번째 커피 까지 마실 수 있을 때 카페인을 정확하게 k만큼 섭취하기 위해 마셔야 하는 커피의 최소 개수이다.```
- K == 0 이면 답은 0 이다.
- sum(C) < K이면 모든 커피를 다 마셔도 카페인을 K만큼 섭취할 수 없다.
- 커피가 총 N개이므로 ```dp[k][n] <= N이다.
- ```k<C[n] 이면 n번째 커피를 마실 수 없다.```
    * ```dp[k][n] = dp[k][n-1]```
- n번째 커피를 마실 수 있고, ```dp[k-C[n]][n-1] != N+1 or dp[k][n-1] != N+1``` 즉, 둘 중 하나라도 가능하면
    * ```dp[k][n] = min(dp[k][n-1], dp[k-C[n]][n-1]+1)```
- 위 과정이 끝나고 ```dp[N][K] != N+1```이면 카페인을 K 만큼 섭취할 수 있는 것이고 ```dp[N][K] == 0```이면 카페인을 K만큼 섭취할 수 없는 것이다.
---

### 소스코드
- 메모리 : 40832KB
- 시간 : 1020ms
```Python
import sys
N, K, *C = map(int, sys.stdin.read().split())
if K == 0: print(0); exit()
if sum(C) < K: print(-1); exit()
C.insert(0,0)
dp = [[0]*(N+1)] + [[N+1]*(N+1) for _ in range(K)]
for k in range(1,K+1):
    for n in range(1,N+1):
        if k < C[n]:
            dp[k][n] = dp[k][n-1]
        elif dp[k-C[n]][n-1] != N+1 or dp[k][n-1] != N+1:
            dp[k][n] = min(dp[k][n-1], dp[k-C[n]][n-1]+1)
print(dp[K][N] if dp[K][N] != N+1 else -1)
```
---
## 풀이 2 - DP(1차원)

### 코드 설명
- ```dp[k]는 카페인을 정확히 k만큼 섭취하기 위해 마셔야 하는 커피의 최소 개수이다.```
- K == 0 이면 답은 0 이다.
- sum(C) < K이면 모든 커피를 다 마셔도 카페인을 K만큼 섭취할 수 없다.
- 각 커피에 대하여 루프를 돌면서 마실 수 있는 경우 ```dp[k]와 dp[k-C[n]]+1을 비교하여 더 작은 값을 dp[k]에 저장한다.```
- ```dp[K] != N+1이면 카페인을 정확히 K만큼 섭취할 수 있다.```
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 552ms
```Python
import sys
N, K, *C = map(int, sys.stdin.read().split())
if K == 0: print(0); exit()
if sum(C) < K: print(-1); exit()
C.insert(0,0)
dp = [N+1]*(K+1)
dp[0] = 0
for n in range(1,N+1):
    for k in range(K,C[n]-1,-1):
        dp[k] = min(dp[k], dp[k-C[n]] + 1)
print(dp[K] if dp[K] != N+1 else -1)
```