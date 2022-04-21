import sys
def input():
    return sys.stdin.readline()
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
P = [0]*(N**2+1)
for i in range(N**2):
    P[i] = P[i-1]+A[i//N][i%N]
ans = -1000*N**2
for n in range(1,N+1):
    for i in range(N-n+1):
        for j in range(N-n+1):
            profit = 0
            for k in range(n):
                profit += P[(i+k)*N+j+n-1] - P[(i+k)*N+j-1]
            ans = max(ans, profit)
print(ans)