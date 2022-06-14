import sys
from heapq import *
input = sys.stdin.readline
N, D = map(int, input().split())
graph = [[(i+1,1)] for i in range(D)]+[[]]

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        graph[s].append((e,d))

distance = [D]*(D+1)
H = []
heappush(H, (0,0))
while H:
    d, pos = heappop(H)
    if distance[pos] >= d:
        for end, length in graph[pos]:
            dist = d + length
            if distance[end] > dist:
                distance[end] = dist
                heappush(H, (dist, end))
print(distance[D])