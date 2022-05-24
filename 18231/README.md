# 백준 10713번 파괴된 도시
https://www.acmicpc.net/problem/10713
---

### 문제 해결 날짜
- 2022.05.21
---

### 접근 방식
- 폭탄을 떨어뜨릴 수 있는 모든 도시에 폭탄을 투하한다.
- `G[n]`은 도시 n과 근접한 도시의 리스트이다.
- D는 파괴된 도시의 집합이다. 따라서 도시 n이 D에 있고, `d=set(G[n])`인 d가 D의 부분집합이면 n에 폭탄을 떨어뜨릴 수 있으므로 bomb에 n을 추가하고, DD에서 n과 d를 제거한다.(DD는 D에서 파괴된 도시를 제거한 집합이다.)
- 위 과정을 D의 요소 n에 대하여 반복한 후에 DD가 공집합이면 지도와 같은 모양이 가능하므로 len(bomb)와 `*bomb`를 출력한다. 아니면 지도와 같은 모양이 불가능한 것이므로 -1을 출력한다.
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
            try: DD.remove(n)
            except: pass
if DD:
    print(-1)
else:
    print(len(bomb))
    print(*bomb)
```