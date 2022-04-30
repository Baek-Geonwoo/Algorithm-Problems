import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [0]*M
for _ in range(N):
    A = list(map(int,input().split()))
    for i in range(M):
        if i == 0:
            dp[i] += A[i]
        else:
            dp[i] = A[i] + max(dp[i], dp[i-1])
print(dp[M-1])