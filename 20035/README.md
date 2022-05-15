# 백준 20035번 이동하기 5
https://www.acmicpc.net/problem/20035
---

### 문제 해결 날짜
- 2022.05.15
---

### 코드 설명
- A가 큰 경로로 이동해야 결과가 커지고, 그 다음 B가 큰 경로로 이동해야한다.
---

### 소스코드
- 메모리 : 33880 KB
- 시간 : 100 ms
```Python
import sys
def I():
    return map(int, sys.stdin.readline().split())
N, M = I()
A = list(I())
B = list(I())
m = max(A)
lo = A.index(m)
hi = N-1-list(reversed(A)).index(m)
print((sum(A)+m*(M-1))*10**9+sum(B)+B[0]*lo+max(B)*(hi-lo)+B[-1]*(N-1-hi))
```
---

### 오답 노트
- 시간 초과
- 1차원 dp테이블을 사용하는 동적 프로그래밍으로 풀려고 했다.
- 시간복잡도가 O(NM)이고 N<=10^5, M<=10^5이므로 MN<=10^10 이라서 시간초과가 발생했다.

### 오답 코드
```Python
import sys
from copy import deepcopy
def I():
    return map(int, sys.stdin.readline().split())
N, M = I()
A = list(I())
B = list(I())
curr = [[A[0],b] for b in B]
for i in range(1,N):
    pre = deepcopy(curr)
    curr[0] = [pre[0][0]+A[i],pre[0][1]+B[0]]
    for j in range(1,M):
        if pre[j] > curr[j-1]:
            curr[j] = [pre[j][0]+A[i], pre[j][1]+B[j]]
        else:
            curr[j] = [curr[j-1][0]+A[i], curr[j-1][1]+B[j]]
a, b = curr[-1]
print(a*10**9+b)
```