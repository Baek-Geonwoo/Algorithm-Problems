# 백준 20002번 사과나무
https://www.acmicpc.net/problem/20002
---

### 문제 해결 날짜
- 2022.04.21
---

### 코드 설명
- `A는 사과나무의 총이익들이 저장된 2차원 리스트이고 A[0][0]부터 A[i][j]까지의 총이익의 합을 P[i*N+j]에 저장한다. 역으로 P[x]는 A[0][0]부터 A[x//N][x%N]까지의 총이익의 합이다`
- 1x1 크기부터 NxN 크기까지 크기를 늘려가며 해당 범위의 총이익의 합의 최댓값을 찾는다.
- nxn범위의 총이익의 합을 구할 때 2중 루프를 쓰면 시간복잡도가 O(N^5)가 되어 시간초과가 발생하므로 A를 탐색하여 nxn번 연산하는 것이 아니라 P를 사용하여 가로 한줄씩 n번 나누어 nxn 범위의 총이익의 합을 구한다.
---

### 소스코드
- 메모리 : 116716KB
- 시간 : 2904ms
```Python
import sys
def input():
    return sys.stdin.readline()
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
P = [0]*(N**2+1)
for i in range(N**2):
    P[i] = P[i-1]+A[i//N][i%N]
ans = -1000*N**2
for n in range(1,N+1):
    for i in range(N-n+1):
        for j in range(N-n+1):
            profit = 0
            for k in range(n):
                profit += P[(i+k)*N+j+n-1] - P[(i+k)*N+j-1]
            ans = max(ans, profit)
print(ans)
```