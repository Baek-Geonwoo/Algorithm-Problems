# 백준 1198번 삼각형으로 자르기
https://www.acmicpc.net/problem/1198
---

### 문제 해결 날짜
- 2022.08.15
---

### 코드 설명
- 다각형에서 삼각형들을 제외하고 남은 마지막 삼각형은 다각형의 점 N개 중 3개로 이루어진 삼각형 중 하나이므로 이 삼각형들의 넓이 중 최댓값이 답이다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 84 ms
```Python
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
ans = 0
polygon = [[int(e) for e in input().split()] for _ in range(N)]

for a,b,c in combinations(polygon, 3):
    triangle = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    triangle -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    triangle = abs(triangle)/2
    ans = max(ans, triangle)
print(ans)
```