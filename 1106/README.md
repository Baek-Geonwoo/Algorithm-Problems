# 백준 1106번 호텔
https://www.acmicpc.net/problem/1106
---

### 문제 해결 날짜
- 2021.03.18
---

### 코드 설명
- ```P[i]는 고객을 i명이상 늘리기 위해 필요한 (최소비용, 늘릴 수 있는 고객수)```
- A에서 비용이 가장 적은 튜플 m을 구하여 ```P[1] = m(늘릴 수 있는 고객수는 자연수이므로)```
- 2부터 C까지 i로 순회하며 다음을 반복한다. ```P[i] = P[i-1]로 초기화하고, P[i-1][1] >= i가 아니면 다음을 시행한다.```
    + ```P[i] = P[i][0]+100, P[i][1]+1로 초기화한다.(P[i-1]을 토대로 비용은 최대로, 사람 수는 최소로)```
    + A를 k로 순회하며 ```i <= A[k][1]이고, P[i][0] > A[k][0]인 k가 있는지 찾고 있다면 P[i] = A[k]로 P[i] 초기화```
    + 1부터 i-1까지 j로 순회하며 다음 두 조건을 만족시키면 ```P[i] = P[i-j][0] + P[j][0], P[i-j][1] + P[j][1]```
        * ```i <= P[i-j][1] + P[j][1]```
        * ```P[i][0] > P[i-j][0] + P[j][0]```
- 시간복잡도 : ```O(C*(C+N)), N이 20이하의 자연수이고, 최악의 경우 C가 N보다 훨씬 크므로 상수취급하면 O(C^2)```
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 304ms
```Python
import sys
I = sys.stdin.readline
C, N = map(int, I().split())
A = []
m = 100, 0
for _ in range(N):
    A.append(tuple(map(int, I().split())))
    if A[-1][0] < m[0]:
        m = A[-1][0], A[-1][1]
P = [0]*(C+1) #P[i]는 고객을 i명이상 늘리기 위해 필요한 (최소비용, 늘릴 수 있는 고객수)
P[1] = m
for i in range(2,C+1):
    P[i] = P[i-1]
    if P[i-1][1] < i:
        P[i] = P[i][0]+100, P[i][1]+1
        for k in range(N):
            if i <= A[k][1] and P[i][0] > A[k][0]:
                P[i] = A[k]
        for j in range(1,i):
            if i <= P[i-j][1] + P[j][1] and P[i][0] > P[i-j][0] + P[j][0]:
                P[i] = P[i-j][0] + P[j][0], P[i-j][1] + P[j][1]
print(P[C][0])
```