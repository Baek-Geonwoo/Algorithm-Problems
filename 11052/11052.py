import sys
N, *P = map(int, sys.stdin.read().split())
P = [0]+P
dp = [0]*(N+1)
dp[1] = P[1]
for i in range(2,N+1):
    dp[i] = P[i]
    for j in range(1,i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])
print(dp[N])