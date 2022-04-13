# 백준 2240번 자두나무
https://www.acmicpc.net/problem/2240
---

### 문제 해결 날짜
- 2022.04.13
---

### 코드 설명
- ```P[t][w]는 t초까지 w번 움직였을 때 받을 수 있는 자두의 최대 개수이다.```
- ```P[t][w] = max(P[t-1][w],P[t-1][w-1]) + int(A[t-1]%2 == (w+1)%2)```
    * t-1초까지 w번 움직이고 1초 기다리거나, t-1초까지 w-1번 움직이고 한 번 더 움직이면 t초까지 w번 움직일 수 있고, ```int(A[t-1]%2 == (w+1)%2)```로 w번 움직였을 때 자두를 받을 수 있는지 구하여 받을 수 있으면 1을 더한다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 80ms
```Python
import sys
T, W, *A = map(int, sys.stdin.read().split())
# P[t][w]는 t+1초까지 w번 움직여 받을 수 있는 자두의 최대 개수
P = [[0]*(W+1) for _ in range(T+1)]
for t in range(1,T+1):
    P[t][0] = P[t-1][0] + int(A[t-1] == 1)
    for w in range(1,W+1):
        P[t][w] = max(P[t-1][w],P[t-1][w-1]) + int(A[t-1]%2 == (w+1)%2)
print(max(P[-1]))
```