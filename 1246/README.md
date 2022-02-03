# 백준 1246번 온라인 판매
https://www.acmicpc.net/problem/1246
---

### 문제 해결 날짜
- 2021.02.01
---

### 접근 방식
- 그리디 기준 : 달걀을 고객이 부른 가격 중 낮은 가격부터 예상수익을 계산한다.
- 고객이 부른 가격들의 리스트 P를 오름차순으로 정렬한다.
- 달걀을 N개를 넘어서 판매할 수 없고, ```달걀 가격이 P[i]일 때 달걀을 살 수 있는 고객은 M-i명 이므로```예상 수익은 고객이 제시한 가격```인 P[i]를 이용해 P[i] * min(N, M-i)```이다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
N, M = map(int, I().split())
P = [int(I()) for _ in range(M)]
P.sort()
price, profit = 0, 0
for i in range(M):
    curr = P[i]*min(N,M-i)
    if curr > profit:
        profit = curr
        price = P[i]
print(price, profit)
```