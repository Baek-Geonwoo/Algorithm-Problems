# 백준 1700번 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
---

### 문제 해결 날짜
- 2022.08.16
---

### 코드 설명
- 멀티탭이 가득 차면, 멀티탭에 꽂혀 있는 기구 중 현재 상태에서 가장 나중에 사용하는 기구를 뽑는다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 72 ms
```Python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
D = [int(e) for e in input().split()]
slot = []
ans = 0

for i, d in enumerate(D):
    if d in slot:
        continue

    if len(slot) < N:
        slot.append(d)
        continue

    slot_idx = []
    for j, s in enumerate(slot):
        if s in D[i:]:
            slot_idx.append(D[i:].index(s))
        else:
            slot_idx.append(101)
            break
    del slot[slot_idx.index(max(slot_idx))]
    slot.append(d)
    ans += 1

print(ans)
```

---
## 오답노트
- 잘못된 그리디 기준을 사용했다.
- 현재 상태에서 사용횟수가 가장 적은 기구를 멀티탭에서 빼는 방식을 사용했다.
- 반례: 사용 횟수가 가장 많이 남았지만 맨 뒤에 사용 횟수가 몰려 있는 경우 상당히 오랫동안 자리 하나를 못쓰게 된다.

### 오답 코드
```Python
import sys
from collections import Counter
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
A = [int(e) for e in input().split()]
C = dict(Counter(A))
ans = 0
H = []
slot = set()
for a in A:
    C[a] -= 1
    if a in slot:
        continue
    if len(slot) == N:
        use, kind = heapq.heappop(H)
        slot.remove(kind)
        ans += 1
    slot.add(a)
    heapq.heappush(H, [C[a], a])
print(ans)
```