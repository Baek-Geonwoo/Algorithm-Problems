import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = {}
distance = {}
for _ in range(M):
	start, end, fare = map(int, input().split())
	if start not in graph:
		graph[start] = {}
	if start not in distance:
		distance[start] = 100000*N
	if end not in distance:
		distance[end] = 100000*N
	if end in graph[start]:
		graph[start][end] = min(graph[start][end], fare)
	else:
		graph[start][end] = fare

start, end = map(int, input().split())
H = [(0, start)]
while H:
	fare, curr = heappop(H)
	if distance[curr] >= fare and curr in graph:
		for e, f in graph[curr].items():
			if distance[e] > f + fare:
				distance[e] = f + fare
				heappush(H, (distance[e], e))
print(distance[end])