# 백준 3079번 입국심사
https://www.acmicpc.net/problem/3079
---

### 문제 해결 날짜
- 2021.03.26
---

### 코드 설명
- check(K)는 K초 동안 M명의 사람이 입국심사를 받을 수 있는지를 구하여 반환하는 함수이다.
- Tk <= 10^9, M <= 10^9이기 때문에 입국심사에는 최대 10^18초가 필요하므로 hi=10^18이다.
- 이분탐색으로 M명의 사람이 입국심사를 받을 수 있는 최소 시간을 구한다.
---

### 소스코드
- 메모리 : 42028KB
- 시간 : 740ms
```Python
import sys
def check(K):
    cnt = 0
    for t in T:
        cnt += K // t
    if cnt >= M: return True
    return False
N, M, *T = map(int, sys.stdin.read().split())
lo, hi = 0, int(1e18)
while lo+1<hi:
    mid = (lo + hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
```