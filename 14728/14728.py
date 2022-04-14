import sys
I = sys.stdin.readline
N, T = map(int, I().split())
A = [0]+[tuple(map(int, I().split())) for _ in range(N)]
dp = [[0]*(T+1) for _ in range(N+1)]
# dp[n][t]는 n번째 단원까지 공부할 수 있고, t시간만큼 공부할 수 있을 때 받을 수 있는 최대 점수
for n in range(1,N+1):
    for t in range(1,T+1):
        if A[n][0] <= t:
            dp[n][t] = max(A[n][1] + dp[n-1][t-A[n][0]], dp[n-1][t])
        else:
            dp[n][t] = dp[n-1][t]
print(dp[N][T])