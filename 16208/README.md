# 백준 16208번 귀찮음
https://www.acmicpc.net/problem/16208
---

### 문제 해결 날짜
- 2022.04.02
---

### 코드 설명
- x+y=n일 때, ```x*y```가 가장 작으려면 x가 매우 작고 y가 매우 커야 한다.
- 가장 짧은 막대부터 자른다.
---

### 소스코드
- 메모리 : 69028KB
- 시간 : 340ms
```Python
import sys
n, *A = map(int, sys.stdin.read().split())
A.sort()
ans = 0
curr = sum(A)
for i in range(n-1):
    curr -= A[i]
    ans += A[i]*curr
print(ans)
```