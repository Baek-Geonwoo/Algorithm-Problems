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