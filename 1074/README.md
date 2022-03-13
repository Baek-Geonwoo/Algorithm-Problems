# 백준 1074번 Z
https://www.acmicpc.net/problem/1074
---

### 문제 해결 날짜
- 2021.03.13
---

### 코드 설명
- ```2^N*2^N```범위를 4개로 나누어 각각 ```1~4 사분면이라 한다.```
- r,c가 있는 범위의 사분면을 찾아 그 사분면을 재귀로 탐색한다.
- ```리턴 값에 (i*2+j)*n**2```을 더한다. (r,c가 그 범위에 해당하지는 않지만 그 전에 방문한 칸의 개수를 더한다.)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
def Z(n, r, c):
    if n == 0:
        return 0
    for i in range(2):
        for j in range(2):
            if r < (i+1)*n and c < (j+1)*n:
                return (i*2+j)*n**2 + Z(n//2, r-i*n, c-j*n)
N, r, c = map(int, sys.stdin.readline().split())
print(Z(2**(N-1),r,c))
```