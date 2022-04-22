# 백준 1010번 다리 놓기
https://www.acmicpc.net/problem/1010
---

### 문제 해결 날짜
- 2022.04.22
---

### 코드 설명
- N <= M이므로 다리를 놓을 수 있는 경우의 수는 MCN이다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 76ms
```Python
import sys
input = sys.stdin.readline
def f(n):
    if n <= 1:
        return 1
    return n*f(n-1)
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    N, M = min(N, M), max(N, M)
    print(f(M)//(f(N)*f(M-N)))
```