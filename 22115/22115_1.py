import sys
N, K, *C = map(int, sys.stdin.read().split())
if K == 0: print(0); exit()
if sum(C) < K: print(-1); exit()
C.insert(0,0)
dp = [[0]*(N+1)] + [[N+1]*(N+1) for _ in range(K)]
for k in range(1,K+1):
    for n in range(1,N+1):
        if k < C[n]:
            dp[k][n] = dp[k][n-1]
        elif dp[k-C[n]][n-1] != N+1 or dp[k][n-1] != N+1:
            dp[k][n] = min(dp[k][n-1], dp[k-C[n]][n-1]+1)
print(dp[K][N] if dp[K][N] != N+1 else -1)