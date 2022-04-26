# 백준 23823번 초코칩 케이크
https://www.acmicpc.net/problem/23823
---

### 문제 해결 날짜
- 2022.04.26
---

### 코드 설명
- `cake[1], cake[2]`에 가로줄, 세로줄을 딕셔너리로 저장한다.
- t, a를 q번 입력받으면서 cake를 업데이트한다.
- cake의 가로, 세로의 최댓값과 최댓값인 행,열의 수를 각각 MAX와 cnt에 저장한다.
- `cnt[1]*cnt[2] == 0`이면 가로나 세로만 있는 것이므로 `(cnt[1]+cnt[2])*n`을 출력한다.
- `cnt[1]*cnt[2] != 0`이면 가로, 세로의 최댓값이 있는 줄들이 겹치는 조각 수 `cnt[1]*cnt[2]`를 출력한다.
---

### 소스코드
- 메모리 : 36316KB
- 시간 : 308ms
```Python
import sys
from collections import defaultdict
def two():
    return map(int, sys.stdin.readline().split())

n, q = two()
cake = {1:defaultdict(int), 2:defaultdict(int)}
MAX = {1:0, 2:0}
cnt = {1:0, 2:0}
for _ in range(q):
    t, a = two()
    cake[t][a] += 1
    if cake[t][a] > MAX[t]:
        MAX[t] = cake[t][a]
        cnt[t] = 1
    elif cake[t][a] == MAX[t]:
        cnt[t] += 1
    if cnt[1]*cnt[2]:
        print(cnt[1]*cnt[2])
    else:
        print((cnt[1]+cnt[2])*n)
```
---

### 오답 노트
- 시간 초과
- h와 v를 구하는 과정에서 루프가 많이 발생해 시간복잡도가 `O(q*n^2)`가 나와 시간초과가 발생했다.

### 오답 코드
```Python
import sys
from collections import defaultdict
def two():
    return map(int, sys.stdin.readline().split())

n, q = two()
cake = [0,defaultdict(int), defaultdict(int)]
for _ in range(q):
    t, a = two()
    cake[t][a] += 1
    h, v = [len([k for k, v in cake[i].items() if max(cake[i].values()) == v]) for i in range(1,3)]
    if not h*v:
        print((h+v)*n)
    else:
        print(h*v)
```