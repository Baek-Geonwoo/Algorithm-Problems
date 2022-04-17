# 백준 2073번 수도배관공사
https://www.acmicpc.net/problem/2073
---

### 문제 해결 날짜
- 2022.04.18
---

### 코드 설명
- ```dp[d]는 수도관 길이를 정확히 d로 할 때 가능한 최대 수도관 용량이다.```
- ```dp[L] = max(dp[L], C)로 초기화한다.```
- ```dp[d] = max(dp[d], min(dp[d-A[p][0]],A[p][1]))```
- ```길이 합이 D가 되게 하는 수도관의 부분집합이 적어도 하나 존재하므로 dp[D] == 0인 경우는 없다.```
- ```d를 D부터 L까지 감소시키면서 루프를 도는 이유는 L부터 D까지 증가시키면서 루프를 돌면 같은 파이프를 여러번 쓰는 경우가 포함될 수 있기 때문이다.```
---

### 소스코드
- 메모리 : 115272KB
- 시간 : 268ms
```Python
import sys
input = sys.stdin.readline
D, P = map(int, input().split())
dp = [0]*(D+1)
for _ in range(P):
    L, C = map(int, input().split())
    dp[L] = max(dp[L], C)
    for d in range(D,L-1,-1):
        dp[d] = max(dp[d], min(dp[d-L],C))
print(dp[D])
```
---

### 오답 노트
- 시간 초과
- 값들을 배열에 입력받은 다음 다시 꺼내서 사용했기 떄문에 시간초과가 발생했다.

### 오답 코드
```Python
import sys
input = sys.stdin.readline
D, P = map(int, input().split())
A = [0] + [tuple(map(int, input().split())) for _ in range(P)]
dp = [0]*(D+1)
for p in range(1,P+1):
    for d in range(D,A[p][0]-1,-1):
        if dp[d] != 0:
            dp[d] = max(dp[d], min(dp[d-A[p][0]],A[p][1]))
        else:
            dp[d] = A[p][1]
print(dp[D])
```