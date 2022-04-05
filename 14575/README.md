# 백준 14575번 뒤풀이
https://www.acmicpc.net/problem/14575
---

### 문제 해결 날짜
- 2022.04.05
---

### 코드 설명
- check(m)은 S를 m으로 했을 때 문제의 조건을 모두 충족시킬 수 있는지를 반환하는 함수이다. 하나라도 l이 S보다 크면 거짓, 마실 수 있는 술의 최대, 최소를 구하여 T가 그 사이에 있으면 참, 아니면 거짓 리턴
- S보다 큰 l이 있거나 T가 마실 수 있는 술의 범위에 없으면 범위의 최소를 키우고, 문제의 조건을 충족하는 것이 가능하면 범위의 최대를 줄인다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
def check(s):
    L, R = 0, 0
    for l,r in A:
        if l <= s:
            L += l; R += min(r,s)
        else: return False
    if L <= T <= R:
        return True
    else:
        return False
I = sys.stdin.readline
N, T = map(int, I().split())
A = [tuple(map(int, I().split())) for _ in range(N)]
lo, hi = 1, 1000000
while lo<=hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid-1
    else:
        lo = mid+1
print(-1 if lo == 1000001 else lo)
```