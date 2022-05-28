# 백준 10427번 빚
https://www.acmicpc.net/problem/10427
---

### 문제 해결 날짜
- 2022.05.28
---

### 접근 방식
- 빚이 {a, b, c}이면(a가 최댓값) M=3일 때 추가로 갚아야 하는 금액은 다음과 같다.
    * 추가로 갚아야 하는 금액 = (a-a) + (a-b) + (a-c)
- 따라서 최댓값과 나머지 값들의 차이가 작을수록 좋으므로 A를 정렬한다.
- A의 prefix-sum을 P에 저장하고 `A[i-M+1]...A[i]`의(M개) 합을 `P[i]-P[i-M]`으로 구하는데 i를 M-1부터 N-1까지 변화시키며 그중 최솟값을 `S[M]`에 저장한다.
- sum(S)를 출력한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 4020 ms
```Python
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, *A = map(int, input().split())
    A.sort()
    P = [0]*(N+1)
    for i in range(N):
        P[i] = P[i-1] + A[i]
    S = [0,0] + [10000*N]*(N-1)
    for M in range(2,N+1):
        for i in range(M-1,N):
            S[M] = min(S[M], A[i]*M - (P[i]-P[i-M]))
    print(sum(S))
```