# 백준 13706번 제곱근
https://www.acmicpc.net/problem/13706
---

### 문제 해결 날짜
- 2022.04.23
---

### 접근 방식
- N 길이가 800자리이면 OverflowError가 발생할 수 있으므로 이분탐색으로 N의 제곱근을 구한다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 80ms
```Python
import sys
N = int(sys.stdin.readline())
lo, hi = 1, N
while lo<=hi:
    mid = (lo+hi)//2
    if N <= mid**2:
        hi = mid-1
    else:
        lo = mid+1
print(lo)
```
---

### 오답 노트
- OverflowError
- Python float은 800자리를 넘을 수 없다.

### 오답 코드
```Python
import sys
N = int(sys.stdin.readline())
print(int(N**0.5))
```