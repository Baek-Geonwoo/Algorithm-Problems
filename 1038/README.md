# 백준 1038번 감소하는 수
https://www.acmicpc.net/problem/1038
---

### 문제 해결 날짜
- 2022.05.12
---

### 접근 방식
- d자리 감소하는 수의 맨 앞자리 숫자는 d-1이상이어야 하므로 d자리 감소하는 수의 시작 숫자는 d-1 ~ 9이다.
- 감소하는 수를 하나 찾을 때마다 N을 감소시키고 N == 0이 될 때 그 수를 출력한다.(N이 0으로 주어질 때를 해결하기 위해 N+1했다.)
- N이 양수이면 N번째 감소하는 수가 없다는 것이므로 -1을 출력한다.
- 감소하는 수는 9876543210이 최대이므로 1자리부터 10자리까지 있다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 72ms
```Python
import sys
def check(X, digit):
    global N
    if N <= 0: return
    if digit == 1:
        N -= 1
        if N == 0:
            print(X)
    else:
        for i in range(int(X[-1])):
            check(X+str(i), digit-1)
def backtrack(digit):
    global N
    if N <= 0: return
    for i in range(digit-1,10):
        check(str(i), digit)
N = int(sys.stdin.readline())+1
for i in range(1,11):
    backtrack(i)
if N>0:
    print(-1)
```