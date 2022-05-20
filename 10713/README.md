# 백준 10713번 기차 여행
https://www.acmicpc.net/problem/10713
---

### 문제 해결 날짜
- 2022.05.20
---

### 코드 설명
- `C[i]`에는 도시 i에서 기차를 타는 횟수가 저장된다.(거처가는 경우는 이전 도시에서 출발하므로 제외), 음수인 경우는 해당 도시에서 내리는 경우이다.
- cnt에는 현재 도시에서 출발하는 기차를 타는 횟수가 저장되어 있으므로 cnt를 기준으로 IC카드를 사서 타는 경우와 IC카드를 사지 않고 타는 경우를 비교하여 더 적은 비용이 들도록 ans에 더한다.
---

### 소스코드
- 메모리 : 57672 KB
- 시간 : 428 ms
```Python
import sys
def input():
    return list(map(int,sys.stdin.readline().split()))
N, M = input()
P = input()
T = [input() for _ in range(N-1)]
C = [0]*N
for i in range(M-1):
    s = min(P[i], P[i+1])-1
    e = max(P[i], P[i+1])-1
    C[s] += 1
    C[e] -= 1
ans = 0
cnt = 0
for i in range(N-1):
    cnt += C[i]
    ans += cnt*T[i][0] if cnt*T[i][0] <= cnt*T[i][1]+T[i][2] else cnt*T[i][1]+T[i][2]
print(ans)
```
---

### 오답 노트
- 시간 초과
- 시간복잡도가 O(N^2)인데 N<=100000이라서 시간초과가 발생했다.

### 오답 코드
```Python
import sys
def input():
    return list(map(int,sys.stdin.readline().split()))
N, M = input()
P = input()
T = [input() for _ in range(N-1)]
C = [0]*(N-1)
prev = P[0]
for i in range(1,M):
    if prev != P[i]:
        for j in range(min(prev,P[i])-1, max(prev,P[i])-1):
            C[j] += 1
        prev = P[i]
ans = 0
for i in range(N-1):
    ans += C[i]*T[i][0] if C[i]*T[i][0] <= C[i]*T[i][1]+T[i][2] else C[i]*T[i][1]+T[i][2]
print(ans)
```