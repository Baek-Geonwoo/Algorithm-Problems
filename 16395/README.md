# 백준 16395번 파스칼의 삼각형
https://www.acmicpc.net/problem/16395
---

### 문제 해결 날짜
- 2021.02.05
---

### 접근 방식
- ```C[i][j] = iCj이고, C[i]의 크기는 i+1이다.```
- j=0 또는 j=i이면 iCj=1이므로 모든 ```C[i]```는 1로 초기화한다.
- iCj = i-1Cj-1 + i-1Cj이므로 ```C[i][j] = C[i-1][j-1] + C[i-1][j]```이다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
n, k = map(int, sys.stdin.readline().split())
C = [[1]*(i+1) for i in range(n)]
for i in range(2,n):
    for j in range(1,i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]
print(C[n-1][k-1])
```