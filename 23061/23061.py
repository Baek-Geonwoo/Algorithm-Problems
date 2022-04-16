import sys
input = sys.stdin.readline
N, M = map(int, input().split())
V, W = [0]*(N+1), [0]*(N+1)
for i in range(1,N+1):
    W[i], V[i] = map(int, input().split())
K = [0]+[int(input()) for _ in range(M)]
k = max(K)
dp = [0]*(k+1)
for n in range(1,N+1):
    for b in range(k, W[n]-1,-1):
        dp[b] = max(dp[b], dp[b-W[n]]+V[n])
ans = 1
for i in range(2, M+1):
    eff1 = dp[K[ans]]/K[ans]
    eff2 = dp[K[i]]/K[i]
    if eff1 < eff2: ans = i
print(ans)