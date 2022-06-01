import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')
V, E = map(int, input().split())
K = int(input())
G = [0] + [[] for _ in range(V)]
distance = [0] + [INF]*V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((w,v))
map(list.sort, G)
distance[K] = 0
H = []
heappush(H, (0,K))
while H:
    w, u = heappop(H)
    if distance[u] < w:
        continue
    for n_w, v in G[u]:
        if distance[v] > n_w + w:
            distance[v] = n_w + w
            heappush(H, (n_w + w,v))
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])