# 백준 17425번 약수의 합
https://www.acmicpc.net/problem/17425
---

### 문제 해결 날짜
- 2022.05.18
---

### 코드 설명
- N<=1000000이므로 M=1000000
- 1은 모든 수의 약수이므로 G를 1로 초기화하고, x가 2부터 M까지 M이하의 x의 배수 y에 대하여 `G[y] += x`한다.
- 2를 제외하고는 n-1이 n의 약수가 되는 경우가 없으므로 `G[x] += G[x-1]`하여 누적합을 이용해 G를 업데이트한다.
---

### 소스코드
- 메모리 : 148436 KB
- 시간 : 260 ms
```Python
import sys
T, *N = map(int, sys.stdin.read().split())
M = 1000000
G = [0] + [1]*M
for x in range(2,M+1):
    d = 1
    while x*d<=M:
        G[x*d] += x
        d += 1
    G[x] += G[x-1]
for n in N:
    print(G[n])
```
---

### 오답 노트
- 시간 초과
- N중 가장 큰 수를 M이라 한다.
- `F[x] = f(x)`
- `G[x] = g(x)`
- x의 약수를 m개라 하면 x의 약수중 m//2개는 sqrt(x) 미만이다.
    * d가 1부터 M까지 `F[x] += d + x//d` 하여 f(x)를 구한 후 G를 업데이트한다.
    * 이때 x가 제곱수이면 제곱근을 `F[x]`에 추가로 더해준다.
- 위 방식으로 했으나 O(N^1.5)라서 시간초과가 발생했다.

### 오답 코드
```Python
import sys
from math import ceil, sqrt
T, *N = map(int, sys.stdin.read().split())
M = max(N)
F = [0]*(M+1)
G = [0]*(M+1)
for x in range(1,M+1):
    for d in range(1,ceil(sqrt(x))):
        if x%d==0:
            F[x] += d+x//d
    if int(sqrt(x)) == sqrt(x):
        F[x] += int(sqrt(x))
    G[x] = G[x-1] + F[x]
for n in N:
    print(G[n])
```