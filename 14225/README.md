# 백준 14225번 부분수열의 합
https://www.acmicpc.net/problem/14225
---

### 문제 해결 날짜
- 2022.04.12
---

### 코드 설명
- S의 각 항을 Sum에 더하거나 더하지 않게 dfs를 호출하고 Sum을 집합 num에 추가하여 num에 S의 부분수열의 합으로 나타낼 수 있는 모든 자연수를 저장한다.
- n=1부터 while 루프를 돌며 num에 없는 자연수를 찾아 출력하고 루프를 종료한다.
---

### 소스코드
- 메모리 : 64636KB
- 시간 : 716ms
```Python
import sys
def dfs(i, Sum):
    if i == N:
        return
    num.add(Sum)
    dfs(i+1, Sum)
    num.add(Sum+S[i])
    dfs(i+1, Sum+S[i])

N, *S = map(int, sys.stdin.read().split())
num = set()
dfs(0,0)
n = 1
while True:
    if n not in num:
        print(n)
        break
    n += 1
```