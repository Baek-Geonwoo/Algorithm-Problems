# 백준 15729번 방탈출
https://www.acmicpc.net/problem/15729
---

### 문제 해결 날짜
- 2021.03.01
---

### 코드 설명
- 문제의 목적은 불이 모두 꺼진 상태에서 쪽지와 똑같은 상태로 만드는 데 필요한 버튼의 최솟값이지만 반대로 쪽지의 상태에서 불이 모두 꺼진 상태로 만드는 횟수와 구하는 값은 같다고 할 수 있다.
- 따라서 가장 왼쪽에 있는 켜져있는 버튼부터 누른다.
---

### 소스코드
- 메모리 : 49744KB
- 시간 : 624ms
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