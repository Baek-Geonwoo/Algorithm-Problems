import sys
T, *N = map(int, sys.stdin.read().split())
M = 1000000
G = [0] + [1]*M
for x in range(2,M+1):
    d = 1
    while x*d<=M:
        G[x*d] += x
        d += 1
    G[x] += G[x-1]
for n in N:
    print(G[n])