# 백준 21317번 징검다리 건너기
https://www.acmicpc.net/problem/21317
---

### 문제 해결 날짜
- 2021.03.09
---

### 코드 설명
- 인덱스 1부터 시작해서 인덱스가 N번 돌에 도착할 때까지 작은 점프, 큰 점프, 매우 큰 점프를 사용해 이동한다. dfs의 각 매개변수는 인덱스, 누적 사용 에너지, 매우 큰 점프 사용여부이다.
- 인덱스가 딱 N이 될 때만(넘으면 그냥 return) ans = min(ans, e)로 ans를 초기화한다.(ans의 초기값은 세 점프의 소모 에너지가 5000이하이므로 ```5000*N```)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 92ms
```Python
import sys
def dfs(idx, e, s):
    global ans
    if idx >= N:
        if idx == N:
            ans = min(ans, e)
        return
    if not s:
        dfs(idx+3,e+K,1)
    dfs(idx+1,e+S[idx][0],s)
    dfs(idx+2,e+S[idx][1],s)
I = sys.stdin.readline
N = int(I())
S = [0] + [tuple(map(int,I().split())) for _ in range(N-1)]
K = int(I())
ans = 5000*N
dfs(1,0,0)
print(ans)
```