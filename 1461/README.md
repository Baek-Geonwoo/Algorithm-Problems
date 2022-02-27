# 백준 1461번 도서관
https://www.acmicpc.net/problem/1461
---

### 문제 해결 날짜
- 2021.02.28
---

### 코드 설명
- 마지막에 0으로 이동할 필요가 없으므로 ans의 초기값을 -B에서 절댓값이 가장 큰 수의 절댓값으로한다.
- p는 B를 오름차순했을 때 가장 작은 양수의 인덱스이다.
- 만약 B에 음수만 있어서 p가 -1일 경우 p를 N으로 초기화한다.
- 양수와 음수에 대하여 M개씩 건너가며 절댓값이 큰 순으로 ans에 더한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
N, M = map(int, I().split())
B = [int(e) for e in I().split()]
B.sort()
ans = -max(abs(B[0]),B[-1])
p = -1
for i in range(N):
    if B[i]>0:
        p = i
        break
if p == -1:
    p = N
for i in range(0,p,M):
    ans += -B[i]*2
for i in range(N-1,p-1,-M):
    ans += B[i]*2
print(ans)
```