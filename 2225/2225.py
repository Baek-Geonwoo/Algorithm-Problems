import sys
N, K = map(int, sys.stdin.readline().split())
P = [0]*(N+1)
P[0] = 1
for k in range(1,K+1):
    for i in range(1,N+1):
        P[i] = (P[i] + P[i-1])%1000000000
print(P[N])