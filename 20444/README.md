# 백준 20444번 색종이와 가위
https://www.acmicpc.net/problem/20444
---

### 문제 해결 날짜
- 2022.04.01

---
### 코드 설명
- mid는 가로 또는 세로로 자른 횟수이다.(가로 세로 구분이 없으므로)
- pieces(mid)는 색종이 조각의 수를 구하여 반환하는 함수이다.
    * n번 잘라야 하므로 세로를 mid번 자른다고 하면 가로는 n-mid번 자르게 되고, 색종이 조각의 수는 ```(mid+1)*(n-mid+1)```개가 된다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
def pieces(mid):
    return (mid+1)*(n-mid+1)
n, k = map(int, sys.stdin.readline().split())
lo, hi = -1, n
while lo+1<hi:
    mid = (lo+hi)//2
    if pieces(mid) == k:
        print('YES'); sys.exit()
    elif pieces(mid) > k: hi = mid
    else: lo = mid
print('NO')
```