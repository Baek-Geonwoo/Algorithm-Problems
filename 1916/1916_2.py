import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [dict() for _ in range(N+1)]
for _ in range(M):
	start, end, fare = map(int, input().split())
	if end in graph[start]:
		graph[start][end] = min(graph[start][end], fare)
	else:
		graph[start][end] = fare
distance = [0] + [100000*N]*N
start, end = map(int, input().split())
H = [(0, start)]
while H:
	fare, curr = heappop(H)
	if distance[curr] >= fare:
		for e, f in graph[curr].items():
			if distance[e] > f + fare:
				distance[e] = f + fare
				heappush(H, (distance[e], e))
print(distance[end])