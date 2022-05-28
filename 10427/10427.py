import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, *A = map(int, input().split())
    A.sort()
    P = [0]*(N+1)
    for i in range(N):
        P[i] = P[i-1] + A[i]
    S = [0,0] + [10000*N]*(N-1)
    for M in range(2,N+1):
        for i in range(M-1,N):
            S[M] = min(S[M], A[i]*M - (P[i]-P[i-M]))
    print(sum(S))