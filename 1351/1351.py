import sys
from collections import defaultdict
def dfs(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = dfs(n//P)+dfs(n//Q)
    return dp[n]
N, P, Q = map(int, sys.stdin.readline().split())
dp = defaultdict(int)
dp[0] = 1
print(dfs(N))