# 백준 9663번 N-Queen
https://www.acmicpc.net/problem/9663
---

### 문제 해결 날짜
- 2021.02.27
---

### 코드 설명
- ```X[i]에는 i번 줄의 퀸의 위치가 저장된다.(X[2]=3이면 위에서부터 3번째 줄의 왼쪽에서부터 4번째 칸에 퀸이 위치)```
- attack함수는 n을 매개변수로 받아 ```X[n]에 위치한 퀸이 X[0]...X[n-1]에 있는 퀸들로 부터 공격받지 않는지를 체크하는 함수이다. 공격받지 않으면 True 받을 수 있으면 False 반환``` i가 0부터 n-1까지
    * ```X[i] == X[n]이면 바로 위이므로 공격받을 수 있다.```
    * ```X[i]+(n-i) == X[n]이면 X[i]가 X[n]의 왼쪽 대각선 위에 있으므로 공격받을 수 있다.```
    * ```X[i]+(n-i) == X[n]이면 X[i]가 X[n]의 오른쪽 대각선 위에 있으므로 공격받을 수 있다.```
- cnt는 현재까지 놓여진 Queen의 개수이며, N == cnt가 참이면 모든 퀸이 놓여진 것이므로 ans += 1한다.
- Python3로는 시간초과가 발생해서 PyPy3으로 제출하여 통과했다.
---

### 소스코드
- 메모리 : 210800KB
- 시간 : 26272ms
```Python
import sys
def attack(n):
    for i in range(n):
        if X[i] == X[n]:
            return False
        if X[i]+(n-i) == X[n]:
            return False
        if X[i]-(n-i) == X[n]:
            return False
    return True
def nqueen(cnt):
    global N, ans
    if N == cnt:
        ans += 1
        return
    for i in range(N):
        X[cnt] = i
        if attack(cnt):
            nqueen(cnt+1)
N = int(sys.stdin.readline())
X = [0]*N
ans = 0
nqueen(0)
print(ans)
```