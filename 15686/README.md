# 백준 15686번 치킨 배달
https://www.acmicpc.net/problem/15686
---

### 문제 해결 날짜
- 2021.02.26
---

### 코드 설명
- 모든 집과 치킨집의 위치(i,j)들을 각각 House와 Chicken에 저장한다.
- ans에 도시의 치킨거리의 최솟값을 저장한다.(ans는 ```N*2*len(House)*len(Chicken) 넘을 수 없으므로 이를 초기값으로 한다.```)
- 1부터 M까지 m(남길 치킨집의 수)으로 순회한다.
    + Chicken에서 중복없이 m개를 고른 모든 크기 m의 리스트에 대하여 C로 순회한다.
        * 위 조건 하에서 치킨 거리를 Distance에 저장한다.
        * House의 집들을 순회하며 모든 치킨집에 대해서 각 집의 치킨거리의 최솟값을 구해 distance에 저장한 후 그 distance의 합을 Distance에 저장한다.(distance의 초기값은 ```N*2을 넘을 수 없으므로 N*2로한다.```)
        * ans = min(ans, Distance)로 초기화한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 2168ms
```Python
import sys
from itertools import combinations
I = sys.stdin.readline
N, M = map(int, I().split())
City = [[int(e) for e in I().split()] for _ in range(N)]
House = []
Chicken = []
for i in range(N):
    for j in range(N):
        if City[i][j] == 1:
            House.append((i,j))
        elif City[i][j] == 2:
            Chicken.append((i,j))
ans = N*2*len(Chicken)
for m in range(1,M+1):
    for C in combinations(Chicken, m):
        Distance = 0
        for hx, hy in House:
            distance = N*2
            for cx, cy in C:
                distance = min(distance, abs(cx-hx)+abs(cy-hy))
            Distance += distance
        ans = min(ans, Distance)
print(ans)
```