import sys
from heapq import *
input = sys.stdin.readline
N, H, T = map(int,input().split())
t = T
G = [-int(input()) for e in range(N)]
heapify(G)
while -G[0]>=H and t:
    if -G[0] == 1:
        break
    g = -heappop(G)
    if g >= H:
        t -= 1
        heappush(G,-(g//2))
if -G[0]<H:
    print('YES')
    print(T-t)
else:
    print('NO')
    print(-G[0])