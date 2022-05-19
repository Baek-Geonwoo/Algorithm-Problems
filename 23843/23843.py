import sys
from heapq import *
input = sys.stdin.readline

N, M = map(int, input().split())
T = sorted(list(map(int, input().split())),reverse=True)
charger = []
for t in T:
    if len(charger) < M:
        heappush(charger, t)
    else:
        heappush(charger, heappop(charger)+t)
print(max(charger))