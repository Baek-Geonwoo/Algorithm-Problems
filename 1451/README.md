# 백준 1451번 직사각형으로 나누기
https://www.acmicpc.net/problem/1451
---

### 문제 해결 날짜
- 2022.05.16
---

### 접근 방식
- 가로나 세로가 3칸 이상이면 NxM 직사각형에 가로로 선을 2개 긋거나 세로로 선을 2개 그어 작은 직사각형 3개로 나눌 수 있다.
- 가로, 세로가 모두 2칸 이상이면 NxM 직사각형에 가로선 1개, 세로선 1개를 그어 직사각형을 4개 만들 수 있다. 이중 이웃한 직사각형 2개를 합치면 NxM 직사각형을 작은 직사각형 3개로 만들 수 있다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 2504 ms
```Python
import sys
from itertools import combinations as comb
input = sys.stdin.readline
N, M = map(int, input().split())
R = [list(map(int,list(input().rstrip()))) for _ in range(N)]
ans = 0
if M >= 3:
    for c in comb(range(1,M), 2):
        rge = [0]+list(c)+[M]
        s = [0]*3
        for n in range(3):
            for i in range(N):
                for j in range(*rge[n:n+2]):
                    s[n] += R[i][j]
        ans = max(ans, s[0]*s[1]*s[2])
if N >= 3:
    for c in comb(range(1,N), 2):
        rge = [0]+list(c)+[N]
        s = [0]*3
        for n in range(3):
            for i in range(M):
                for j in range(*rge[n:n+2]):
                    s[n] += R[j][i]
        ans = max(ans, s[0]*s[1]*s[2])
if N >= 2 and M >= 2:
    for n in range(1,N):
        for m in range(1,M):
            s = [0]*4
            rgeN = [0,n,N]
            rgeM = [0,m,M]
            for nn in range(2):
                for mm in range(2):
                    for i in range(*rgeN[nn:nn+2]):
                        for j in range(*rgeM[mm:mm+2]):
                            s[nn*2+mm] += R[i][j]
            ans = max(ans, (s[0]+s[1])*s[2]*s[3])
            ans = max(ans, s[0]*(s[1]+s[3])*s[2])
            ans = max(ans, s[0]*s[1]*(s[2]+s[3]))
            ans = max(ans, (s[0]+s[2])*s[1]*s[3])
print(ans)
```