import sys
I = sys.stdin.readline
C, N = map(int, I().split())
A = []
m = 100, 0
for _ in range(N):
    A.append(tuple(map(int, I().split())))
    if A[-1][0] < m[0]:
        m = A[-1][0], A[-1][1]
P = [0]*(C+1)
P[1] = m
for i in range(2,C+1):
    P[i] = P[i-1]
    if P[i-1][1] < i:
        P[i] = P[i][0]+100, P[i][1]+1
        for k in range(N):
            if i <= A[k][1] and P[i][0] > A[k][0]:
                P[i] = A[k]
        for j in range(1,i):
            if i <= P[i-j][1] + P[j][1] and P[i][0] > P[i-j][0] + P[j][0]:
                P[i] = P[i-j][0] + P[j][0], P[i-j][1] + P[j][1]
print(P[C][0])