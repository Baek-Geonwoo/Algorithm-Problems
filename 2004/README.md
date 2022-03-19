# 백준 2004번 조합 0의 개수
https://www.acmicpc.net/problem/2004
---

### 문제 해결 날짜
- 2021.03.19
---

### 코드 설명
- get_exp(limit, e)는 limit!의 e의 지수를 구하여 반환하는 함수이다.
- e가 2, 5일 때 둘중 작은 값이 limit!의 0의 개수이다.
- nCm은 n!/m!(n-m)!이므로 limit을 n, m, n-m, e를 2, 5로 하여 n!의 0의 개수에서 m!과 (n-m)!의 0의 개수를 빼서 답을 구한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
def get_exp(limit,e):
    b = e
    ans = 0
    while b <= limit:
        ans += limit//b
        b *= e
    return ans
n, m = map(int, sys.stdin.readline().split())
ans = [get_exp(n,2), get_exp(n,5)]
for x in (m,n-m):
    for i,e in enumerate((2,5)):
        ans[i] -= get_exp(x,e)
print(min(ans))
```