# 백준 2258번 정육점
https://www.acmicpc.net/problem/2258
---

### 문제 해결 날짜
- 2021.03.17
---

### 코드 설명
- 고기 리스트를 가격에 대하여 오름차순, 무게에 대하여 내림차순으로 정렬한다.
- 초기값은 2^32로하고, B를 순회하는데 mass에 현재까지 순회한 고기들의 무게 합, price에 현재까지 고기의 최고가, P는 현재까지 고기를 구매하는 데 필요한 비용의 합이다.(예를 들어, 가격이 22333 이라면 끝까지 순회했을 때 P=9이다. 즉, 비용이 price인 고기 덩어리들의 가격의 합이다.)
- mass가 M 이상이면 ans = min(ans, P)로 초기화한다.
---

### 소스코드
- 메모리 : 54708KB
- 시간 : 340ms
```Python
import sys
I = sys.stdin.readline
N, M = map(int,I().split())
B = [tuple(map(int,I().split())) for _ in range(N)]
B.sort(key= lambda x: (x[1], -x[0]))
ans = 2e32
mass = 0
P, price = 0, 0
for m, p in B:
    if price < p:
        price = p
        P = 0
    mass += m
    P += p
    if mass >= M:
        ans = min(ans, P)
if mass < M:
    print(-1)
else:
    print(ans)
```