# 백준 19940번 피자 오븐
https://www.acmicpc.net/problem/19940
---

### 문제 해결 날짜
- 2021.03.16
---

### 코드 설명
- 5가지 버튼을 눌러야 하는 횟수를 ans에 저장한다.
- h, t, o(각각 60, 10, 1분)을 N//60, (N%60)//10, N%10으로 초기화한다.
- o가 5 초과이면 t를 1증가시키는 것이 전체 횟수도 줄고 사전순으로 더 앞이므로 t += 1, o -= 10
- t가 3 초과이면 마찬가지 이유로 h += 1, t -= 6
- t가 음수이고, o가 5이면 전체횟수가 감소하고, o보다 우선순위가 높은 MINT가 감소하므로 t += 1, o -= 10
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 76ms
```Python
import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    N = int(I())
    ans = [0]*5
    h, t, o = N//60, (N%60)//10, N%10
    if o > 5:
        t += 1
        o -= 10
    if t > 3:
        h += 1
        t -= 6
    if t < 0 and o == 5:
        t += 1
        o -= 10
    ans[0] = h
    ans[2-(t>0)] = abs(t)
    ans[4-(o>0)] = abs(o)
    print(*ans)
```