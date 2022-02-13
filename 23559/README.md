# 백준 23559번 밥
https://www.acmicpc.net/problem/23559
---

### 문제 해결 날짜
- 2021.02.13
---

### 코드 설명
- 예산이 허락하는 한, 맛수치가 높고 싼 메뉴부터 먹는다.
- M을 A-B를 기준으로 내림차순 정렬한다.
- 하루에 1끼를 무조건 먹어야 하므로 모두 B로 먹는다고 가정하고 ```X -= 1000*N```한다.
- M을 a, b로 순회하면서 a > b이고, X>=4000이면 ans에 a를 더하고 X -= 4000, 아니면 b를 더한다.
---

### 소스코드
- 메모리 : 54708KB
- 시간 : 280ms
```Python
from sys import stdin
I = stdin.readline
N, X = map(int, I().split())
M = [list(map(int, I().split())) for _ in range(N)]
M.sort(key = lambda x: -(x[0]-x[1]))
X -= 1000*N
ans = 0
for a, b in M:
    if a > b and X>=4000:
        ans += a
        X -= 4000
    else:
        ans += b
print(ans)
```