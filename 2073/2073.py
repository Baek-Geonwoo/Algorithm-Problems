import sys
input = sys.stdin.readline
D, P = map(int, input().split())
dp = [0]*(D+1)
for _ in range(P):
    L, C = map(int, input().split())
    dp[L] = max(dp[L], C)
    for d in range(D,L-1,-1):
        dp[d] = max(dp[d], min(dp[d-L],C))
print(dp[D])