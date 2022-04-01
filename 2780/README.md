# 백준 2780번 비밀번호
https://www.acmicpc.net/problem/2780
---

### 문제 해결 날짜
- 2021.03.30
---

## 풀이1 - DP+DFS
---
### 코드 설명
- K는 그림의 숫자리스트, pos는 각 숫자의 K(그림)에서의 인덱스를 저장한 사전이다.
- ```dp테이블 P는 P[i][j]: 길이가 i인 j로 끝나는 비밀번호의 개수이다.```
- i가 1이면 ```P[1][j]는 j에 상관없이 1이므로 P[i]를 초기화한다.```
- 2부터 N까지 i로 순회하는 안에서 0에서 9까지 j로 순회하며 dp테이블을 채운다.
- pos에서 숫자 j의 위치를 받아 상하좌우에 있는 숫자들을 찾는다. 그러면 ```P[i][j] += P[i-1][K[nx][ny]]가 성립한다.``` 즉, 길이가 i-1이고, j와 이웃한 숫자로 끝나는 비밀번호들의 개수의 합이 ```P[i][j]```가 된다.
- ```P[i][j]가 너무 커지는 것을 막기 위해 중간에 P[i][j] %= 1234567하고 dp테이블 채우기가 끝나면 sum(P[N])이 N자리 비밀번호의 개수이므로 이를 1234567로 나눈 나머지를 출력한다.```
- 시간복잡도: O(N)
---

### 소스코드
- 메모리 : 130152KB
- 시간 : 660ms
```Python (pypy3)
import sys
def in_range(x,y):
    if x == 3 and y == 0:
        return True
    elif 0<=x<3 and 0<=y<3:
        return True
    return False
T, *L = map(int, sys.stdin.read().split())
d = (-1,0), (1,0), (0,-1), (0,1)
for t in range(T):
    N = L[t]
    P = [[0]*10 for _ in range(N+1)] #P[i][j]는 j로 끝나는 i자리 비밀번호의 수
    P[1] = [1]*10
    K = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
    pos = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        0:(3,0)
        }
    for i in range(2,N+1):
        for j in range(10):
            x, y = pos[j]
            for dx,dy in d:
                nx, ny = x+dx, y+dy
                if in_range(nx,ny):
                    P[i][j] += P[i-1][K[nx][ny]]
            P[i][j] %= 1234567
    print(sum(P[N])%1234567)
```
---

## 풀이2 - DP
---
### 코드 설명
- K는 각 숫자에 인접한 숫자들을 저장한 딕셔너리이다.
- 비밀번호 길이를 2부터 N까지 현재 구하는 비밀번호보다 길이가 1짧은 i로 끝나는 비밀번호의 개수가 ```P[i]```에 저장된다. 현재 구하는 비밀번호의 수는 ```C[i]```에 저장된다.
- ```C[i] = sum([P[k] for k in K[i]])이므로 이를 N-1번 반복하면 sum(C)가 길이가 N인 비밀번호의 개수이다.```
- 시간복잡도: O(N)
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 3064ms
```Python
import sys
T, *L = map(int, sys.stdin.read().split())
K = {
    1:(2,4),2:(1,3,5),3:(2,6),
    4:(1,5,7),5:(2,4,6,8),6:(3,5,9),
    7:(0,4,8),8:(5,7,9),9:(6,8),
    0:(7,)
}
mod = 1234567
for t in range(T):
    N = L[t]
    P = [1]*10
    C = [0]*10
    for _ in range(1,N):
        for i in range(10):
            for k in K[i]:
                C[i] += P[k]
        P = [c%mod for c in C]
        C = [0]*10
    print(sum(P)%mod)
```