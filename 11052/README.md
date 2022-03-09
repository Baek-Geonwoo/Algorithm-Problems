# 백준 11052번 카드 구매하기
https://www.acmicpc.net/problem/11052
---

### 문제 해결 날짜
- 2021.03.10
---

### 코드 설명
- ```dp[i]는 i개의 카드를 사는 데 사용할 수 있는 최대금액이다.```
- ```dp[1]는 P[1]이다.```
- 2부터 N까지 i로 순회하며 다음을 반복한다.
    + ```dp[i]의 초기값은 P[i]```
    + 1부터 i-1까지 j로 순회하며 ```dp[i] = max(dp[i], dp[i-j]+dp[j])```
- 시간복잡도: O(N^2)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 264ms
```Python
import sys
N, *P = map(int, sys.stdin.read().split())
P = [0]+P
dp = [0]*(N+1)
dp[1] = P[1]
for i in range(2,N+1):
    dp[i] = P[i]
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])
print(dp[N])
```