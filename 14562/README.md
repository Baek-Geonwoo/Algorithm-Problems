# 백준 14562번 태권왕
https://www.acmicpc.net/problem/14562
---

### 문제 해결 날짜
- 2021.02.22
---

### 코드 설명
- S, T, k는 각각 태균이의 점수, 상대의 점수, 발차기 횟수이고, ans에는 S == T가 되는 k의 최솟값이 저장된다.(ans의 초기값은 10000으로한다.)
- Q가 빌 때까지 while문에서 다음을 반복한다.(단, 아래 조건문 둘은 조건이 만족되면 둘 다 실행한다.)
    * 만약 S == T라면 ans를 min(ans,k)로 초기화하고 continue한다.
    * S < T이면 Q에 (S+1, T, k+1)을 추가한다.
    * ```S*2<=T+3이면 Q에 (S*2, T+3, k+1)을 추가한다.```
---

### 소스코드
- 메모리 : 32368KB
- 시간 : 272ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
C = int(I())
for _ in range(C):
    S, T = map(int, I().split())
    Q = deque(((S,T,0),))
    ans = 10000
    while Q:
        S, T, k = Q.pop()
        if S == T:
            ans = min(ans,k)
            continue
        if S < T:
            Q.appendleft((S+1, T, k+1))
        if S*2 <= T+3:
            Q.appendleft((S*2, T+3, k+1))
    print(ans)
```