# 백준 16938번 캠프 준비
https://www.acmicpc.net/problem/16938
---

### 문제 해결 날짜
- 2022.05.14
---

### 코드 설명
- A를 정렬한다. A에서 `2~N`개를 뽑아 해당 조합을 c(A가 정렬되어 있으므로 c도 정렬되엉 있다.)라 하면 sum(c)가 L이상 R이하이고, 가장 어려운 문제와 가장 쉬운 문제의 난이도차이(`c[-1]-c[0]`)가 X 이상인지 판단하여 해당되면 ans += 1
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 84 ms
```Python
import sys
from itertools import combinations
input = sys.stdin.readline
N, L, R, X = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(2,N+1):
    for c in combinations(A,i):
        if L <= sum(c) <= R and c[-1]-c[0] >= X:
            ans += 1
print(ans)
```