# 백준 18114번 블랙 프라이데이
https://www.acmicpc.net/problem/18114
---

### 문제 해결 날짜
- 2022.05.02
---

### 코드 설명
- `check[i]`는 물건들의 무게 조합으로 i가 가능한지를 저장하는 리스트이다.
- 각 물건의 무게는 가능하므로 각 `check[물건 무게]=1`
- `check[C]=1이면 1을 출력하고 프로그램 종료`
- 2중 루프로 물건 2개를 고르는 경우와 3개를 고르는 경우를 본다.
- 물건 2개를 구하는 경우 W에서 `i로 range(N), j로 range(i+1,N)`으로 루프를 돌면서 `W[i] + W[j] == C`이면 1을 출력하고 프로그램 종료
    * `W[i] + W[j] < C`이면 `remain = C - W[i] - W[j]`라 하고 `check[remain]=1이면 물건 3개의 무게 조합으로 가능한 경우 이므로 1을 출력하고 프로그램 종료`
---

### 소스코드
- 메모리 : 895924 KB
- 시간 : 712 ms
```Python
import sys
N, C, *W = map(int, sys.stdin.read().split())
check = [0]*100000001
for w in W:
    check[w] = 1
if check[C]:
    print(1)
    sys.exit()
for i in range(N):
    for j in range(i+1,N):
        if W[i] + W[j] == C:
            print(1)
            sys.exit()
        elif W[i] + W[j] < C:
            remain = C - W[i] - W[j]
            if check[remain] and remain not in (W[i], W[j]):
                print(1)
                sys.exit()
print(0)
```
---

### 오답 노트
- 시간 초과
- 시간복잡도가 O(N^2logN)이라 1억 주변이지만 시간초과가 발생했다.

### 오답 코드
```Python
import sys
def binary_search(k, *lst):
    lo, hi = -1, N-1
    while lo+1<hi:
        mid = (lo+hi)//2
        if W[mid] == k:
            if W[mid] not in lst:
                return True
            return False
        elif W[mid] > k:
            hi = mid
        else:
            lo = mid
def solve():
    if binary_search(C):
        return 1
    for w in W:
        if C-w>0 and binary_search(C-w,w):
            return 1
    for a in W:
        for b in W:
            if a != b and C-a-b>0 and binary_search(C-a-b,a,b):
                return 1
    return 0
N, C, *W = map(int, sys.stdin.read().split())
W.sort()
print(solve())
```