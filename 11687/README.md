# 백준 11687번 팩토리얼 0의 개수
https://www.acmicpc.net/problem/11687
---

### 문제 해결 날짜
- 2022.05.27
---

### 접근 방식
- 어떤 수에서 항상 2의지수>=5의지수 이므로 5의 지수의 수가 0의 수이다.
    * `M*=5한다.`
- M == 5의지수 이면 ans에 mid를 저장한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 72 ms
```Python
import sys
def check(m):
    n = 0
    d = 5
    while d<=m:
        n += m//d
        d *= 5
    return n
M = int(sys.stdin.readline())
lo, hi = 1, 500000000
ans = -1
flag = False
while lo<=hi:
    mid = (lo+hi)//2
    n = check(mid)
    if n >= M:
        if M == n:
            ans = mid
            flag = True
        hi = mid-1
    else:
        lo = mid+1
if flag:
    print(ans)
else:
    print(-1)
```