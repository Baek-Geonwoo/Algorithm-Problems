# 백준 19638번 센티와 마법의 뿅망치
https://www.acmicpc.net/problem/19638
---

### 문제 해결 날짜
- 2022.05.09
---

### 코드 설명
- 거인들의 키를 음수로 하여 max heap을 구현하여 센티보다 키가 큰 거인 중 가장 키가 큰 거인부터 뿅망치를 맞도록 한다.
- 뿅망치 횟수를 다 쓰거나, 센티보다 키가 큰 거인이 없는 동안 루프를 돌며 규칙에 맞게 뿅망치를 사용한다.
    * 키가 1인 거인은 뿅망치를 맞아도 키가 줄어들지 않으므로 `-G[0]==1`이면 루프를 종료한다.
- `-G[0]<H`으로 모든 거인이 센티보다 키가 작도록 할 수 있는지 판단한다.
---

### 소스코드
- 메모리 : 36764 KB
- 시간 : 192 ms
```Python
import sys
from heapq import *
input = sys.stdin.readline
N, H, T = map(int,input().split())
t = T
G = [-int(input()) for e in range(N)]
heapify(G)
while -G[0]>=H and t:
    if -G[0] == 1:
        break
    g = -heappop(G)
    if g >= H:
        t -= 1
        heappush(G,-(g//2))
if -G[0]<H:
    print('YES')
    print(T-t)
else:
    print('NO')
    print(-G[0])
```