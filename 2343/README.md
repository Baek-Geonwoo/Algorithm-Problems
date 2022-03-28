# 백준 2343번 기타 레슨
https://www.acmicpc.net/problem/2343
---

### 문제 해결 날짜
- 2021.03.28
---

### 코드 설명
- 블루레이 크기는 sum(B)를 넘을 수 없으므로(넘어가면 낭비) 이분탐색 범위는 0,sum(B)이다.
- 이분탐색 중 check(m)에서 m이 mx=max(B)보다 크면 블루레이 제작이 불가능하므로 False를 리턴, 순서대로 B의 요소들을 순회하며 블루레이의 최소 개수를 구하여 그 수가 M 이하인지를 리턴한다.
---

### 소스코드
- 메모리 : 42028KB
- 시간 : 308ms
```Python
import sys
def check(m):
    if m < mx: return False
    cnt = 1
    curr = 0
    for b in B:
        if curr+b > m:
            cnt += 1
            curr = 0
        curr += b
    if cnt <= M: return True
    return False
N, M, *B = map(int, sys.stdin.read().split())
lo, hi = 0, sum(B)
mx = max(B)
while lo+1<hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
```