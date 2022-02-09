# 백준 16922번 로마 숫자 만들기
https://www.acmicpc.net/problem/16922
---

### 문제 해결 날짜
- 2021.02.09
---

### 코드 설명
- 로마숫자의 순서가 중요하지 않으므로 결론적으로 각 숫자가 몇개 있는지만 알면 된다.
- 따라서 반복문으로 I, V, X의 개수(각각 i,v,x)를 루프를 돌면, L의 개수는 l=N-i-v-x가 되므로 ```ans = 1*i + 5*v + 10*x + 50*l```로 로마숫자로 만들 수 있는 수를 구하고 집합으로 겹치는 수가 없게 한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
N = int(sys.stdin.readline())
S = set()
for i in range(N+1):
    for v in range(N-i+1):
        for x in range(N-i-v+1):
            l = N - i - v - x
            ans = 1*i + 5*v + 10*x + 50*l
            S.add(ans)
print(len(S))
```
---
### 오답노트
- 백트래킹 문제라서 백트래킹으로 풀었더니 시간복잡도가 O(4^N)이 나와서 시간초과가 떴다.

### 오답코드
```Python
import sys
def solution(i):
    global N, ans
    if i == N:
        S.add(ans)
        return
    for r in R:
        ans += r
        solution(i+1)
        ans -= r
N = int(sys.stdin.readline())
S = set()
R = [1, 5, 10, 50]
ans = 0
solution(0)
print(len(S))
```