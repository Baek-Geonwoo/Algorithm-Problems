import sys
N, K, *V = map(int, sys.stdin.read().split())
V.sort()
spd = 0
for i in range(1, N):
    spd = max(V[0]*i+V[i]*(N-i), spd)
print(K//spd if K%spd==0 else K//spd+1)