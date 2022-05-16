# 백준 2015번 수들의 합 4
https://www.acmicpc.net/problem/2015
---

### 문제 해결 날짜
- 2022.05.17
---

### 코드 설명
- A를 순회하면서 pSum에 누적합을 저장하고 dct를 pSum으로 업데이트한다.
- `dct[pSum-K]`가 존재하면 크기가 K인 부분합이 존재하는 것이므로 ans+= `dct[pSum-K]`
---

### 소스코드
- 메모리 : 45056 KB
- 시간 : 180 ms
```Python
import sys
from collections import defaultdict
N, K, *A = map(int, sys.stdin.read().split())
dct = defaultdict(int)
dct[0] = 1
pSum = 0
ans = 0
for a in A:
    pSum += a
    if pSum-K in dct: ans += dct[pSum-K]
    dct[pSum] += 1
print(ans)
```