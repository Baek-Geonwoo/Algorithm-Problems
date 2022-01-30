# 백준 1783번 병든 나이트
https://www.acmicpc.net/problem/1783
---

### 문제 해결 날짜
- 2021.01.25
---

### 접근 방식
- 기본적으로 높이(N)가 충분하면 높이는 위 아래로 이동이 가능하므로 문제의 4가지 이동 중 1,4번 이동만 쓰면 최대한 많은 칸을 방문할 수 있다.
- ans에 병든 나이트가 이동할 수 있는 최대 칸수를 저장한다.
- 병든 나이트의 이동은 다음과 같이 나눌 수 있다.
    * N이 1 이면 이동 자체가 불가능하므로 ans = 1이다.
    * N이 2면 M이 아무리 커도 2,3번 이동은 불가능하고 4가지 이동을 모두 할 수 있는 게 아니므로 최대 4칸을 방문할 수 있다. 따라서 ans = min((M-1)//2+1,4)이다.
    * N이 3 이상인 경우
        + M이 7미만인 경우 병든 나이트가 4번 이동할 동안 4가지 이동을 모두 한번씩 사용할 수 없으므로(최소 3x7칸이 필요하다.) ans = min(M,4)이다.
        + M이 7이상인 경우 병든 나이트가 4가지 이동을 모두 하는데 최소 가로 7칸이 필요하므로 가로 7칸을 이동할 때 병든 나이트가 5칸을 방문하고 나머지 이동은 가로로 1칸만 이동하는 1,4번 이동만 하는 것이 더 많은 칸을 방문할 수 있으므로 ans = M-7+5이다.
---
### 오답노트
- 오답코드
```Python
import sys
N, M = map(int, sys.stdin.readline().split())
ans = 1 # 병든 나이트가 이동할 수 있는 최대 칸수
if N==2:
    ans = (M-1)//2+1
else:
    if M<7:
        ans = min(M,4)
    else:
        ans = M-7+5
print(ans)
```
- 위 코드의 경우 N=1일때는 ans가 무조건 1이어야 하는데 M에 따라 ans가 1이 아니게 될 수 있어 조건문을 수정했다.

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
N, M = map(int, sys.stdin.readline().split())
if N == 1:
    ans = 1
elif N==2:
    ans = min((M-1)//2+1,4)
elif M<7:
    ans = min(M,4)
else:
    ans = M-7+5
print(ans)
```