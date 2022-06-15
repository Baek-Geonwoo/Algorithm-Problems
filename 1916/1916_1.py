import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
	start, end, fare = map(int, input().split())
	graph[start].append((fare, end))
distance = [0] + [100000*N]*N
start, end = map(int, input().split())
H = [(0, start)]
while H:
	fare, curr = heappop(H)
	if distance[curr] >= fare:
		for f, e in graph[curr]:
			if distance[e] > f + fare:
				distance[e] = f + fare
				heappush(H, (distance[e], e))
print(distance[end])