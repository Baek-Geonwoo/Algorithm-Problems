# 백준 18231번 파괴된 도시
https://www.acmicpc.net/problem/18231
---

### 문제 해결 날짜
- 2022.05.21
---

### 코드 설명
- 해당 도시에 연결된 도시가 모두 파괴되었을 경우에 그 도시에 폭탄이 떨어졌을 수 있으므로 이에 해당되는 모든 도시에 폭탄이 떨어졌다고 가정한다.
- 폭탄이 투하되었을 수 있는 모든 도시에 폭탄이 투하되었을 때 파괴된 도시들은 DD에서 제거한다.
- 이러한 과정이 끝나고 DD가 공집합이면 지도와 같은 모양이 나올 수 있는 것이고 아니면 불가능한 것이다.
---

### 소스코드
- 메모리 : 37576 KB
- 시간 : 228 ms
```Python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = [0] + [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
K = int(input())
k = [int(e) for e in input().split()]
D = set(k)
DD = set(k)
bomb = set()
for n in k:
    if n in D:
        d = set(G[n])
        if d.issubset(D):
            DD -= d
            bomb.add(n)
            try:
                DD.remove(n)
            except: pass
if DD:
    print(-1)
else:
    print(len(bomb))
    print(*bomb)
```