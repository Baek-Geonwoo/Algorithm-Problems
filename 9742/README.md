# 백준 9742번 순열
https://www.acmicpc.net/problem/9742
---

### 문제 해결 날짜
- 2021.02.08
---

### 접근 방식
- 입력값 한줄씩 split을 적용하여 S, n에 저장한다. 이때 입력이 종료되면 오류가 발생하므로 try-except를 사용하여 오류가 발생하면 while문을 종료한다.
- ```visited[i]에 ans에 S[i]가 있는지의 여부를 boolean 값으로 저장한다.```
- solve(l)의 l은 현재 ans의 길이를 나타내는 파라미터이다.
- l == len(S)이면 visited로 중복여부를 체크하기 때문에 모든 경우가 다르므로 cnt에 1을 추가하고 만약 cnt == n이면 출력한다음 cnt 여부에 상관없이 종료한다.
- l != len(S)이면 i가 ```0~len(S)-1까지 순회한.```
    + ```visited[i]가 참이면 ans에 S[i]가 포함된 것이므로 continue ```
    + ```포함되지 않으면```
        1. ```ans.append(S[i])하고, visited[i]=True로 초기화한다.```
        2. solve(l+1)을 재귀호출한다.
        3. ```ans.pop()하고, visited[i]=False로 초기화한다.```
---

### 소스코드
- 메모리 : 59208KB
- 시간 : 7212ms
```Python
import sys
I = sys.stdin.readline
def solve(l):
    global visited
    global S
    global cnt, n
    global ans
    if l == len(S):
        cnt += 1
        if cnt == n:
            print(S,n,"=","".join(ans))
        return
    for i in range(len(S)):
        if visited[i]:
            continue
        ans.append(S[i])
        visited[i] = True
        solve(l+1)
        ans.pop()
        visited[i] = False

while True:
    try:
        S, n = I().strip().split()
    except:
        break
    n = int(n)
    f = 1
    for i in range(2,len(S)+1):
        f *= i
    if n > f:
        print("{} {} = No permutation".format(S, n))
        continue
    visited = [False]*n
    ans = []
    cnt = 0
    solve(0)
```