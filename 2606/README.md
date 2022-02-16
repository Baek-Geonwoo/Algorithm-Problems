# 백준 2606번 바이러스
https://www.acmicpc.net/problem/2606
---

### 문제 해결 날짜
- 2021.02.16
---

### 코드 설명
- stack이 빌 때까지 1번 컴퓨터부터 DFS를 통해 탐색한다.
- 1번 컴퓨터부터 DFS를 통해 방문한 모든 컴퓨터가 웜 바이러스에 걸리게 된다.
- 1번 컴퓨터는 제외해야 하므로 ans는 -1부터 시작한다.
---

### 소스코드
- 메모리 : 32368KB
- 시간 : 92ms
```Python
import sys
from collections import deque
I = sys.stdin.readline
N = int(I())
M = int(I())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, I().split())
    G[a].append(b)
    G[b].append(a)
stack = deque([1])
visited = [False]*(N+1)
ans = -1 #1번 컴퓨터를 제외해야 하므로
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        ans += 1
        stack.extend(reversed(G[v]))
print(ans)
```