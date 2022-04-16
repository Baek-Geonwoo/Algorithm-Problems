# 백준 23061번 백남이의 여행 준비
https://www.acmicpc.net/problem/23061
---

### 문제 해결 날짜
- 2022.04.16
---

## 풀이 1 - DP(1차원)

### 코드 설명
- ```dp[b]는 가방에 물건을 무게 b까지 넣을 수 있을 때 가방에 넣을 수 있는 물건의 가치 합의 최댓값이다.```
- ```dp[b] = max(dp[b], dp[b-W[n]]+V[n])```
- 위 과정이 끝나고 각 가방의 효율성(```dp[K[i]]/K[i]```)을 구해서 효율성이 최대인 가방 번호를 ans에 저장하여 출력한다.
---

### 소스코드
- 메모리 : 122304KB
- 시간 : 940ms
```Python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
V, W = [0]*(N+1), [0]*(N+1)
for i in range(1,N+1):
    W[i], V[i] = map(int, input().split())
K = [0]+[int(input()) for _ in range(M)]
k = max(K)
dp = [0]*(k+1)
for n in range(1,N+1):
    for b in range(k, W[n]-1,-1):
        dp[b] = max(dp[b], dp[b-W[n]]+V[n])
ans = 1
for i in range(2, M+1):
    eff1 = dp[K[ans]]/K[ans]
    eff2 = dp[K[i]]/K[i]
    if eff1 < eff2: ans = i
print(ans)
```
---

### 오답 노트
- 시간 초과
- dp 테이블이 2차원이라 구현에 시간이 많이 들어가서 발생했다.

### 오답 코드
```Python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
V, W = [0]*(N+1), [0]*(N+1)
for i in range(1,N+1):
    W[i], V[i] = map(int, input().split())
K = [0] + [int(input()) for _ in range(M)]
k = max(K)
dp = [[0]*(N+1) for _ in range(k+1)]
for b in range(1,k+1):
    for n in range(1,N+1):
        if b < W[n]:
            dp[b][n] = max(dp[b][n], dp[b][n-1])
        else:
            dp[b][n] = max(dp[b][n-1], dp[b-W[n]][n-1]+V[n])
ans = 1
for i in range(2, M+1):
    eff1 = dp[K[ans]][N]/K[ans]
    eff2 = dp[K[i]][N]/K[i]
    if eff1 < eff2: ans = i
print(ans)
```