import sys
N, K, *C = map(int, sys.stdin.read().split())
if K == 0: print(0); exit()
if sum(C) < K: print(-1); exit()
C.insert(0,0)
dp = [N+1]*(K+1)
dp[0] = 0
for n in range(1,N+1):
    for k in range(K,C[n]-1,-1):
        dp[k] = min(dp[k], dp[k-C[n]] + 1)
print(dp[K] if dp[K] != N+1 else -1)