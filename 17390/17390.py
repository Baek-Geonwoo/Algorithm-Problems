import sys
I = sys.stdin.readline
N, Q = map(int, I().split())
A = [int(e) for e in I().split()]
A.sort()
P = A[:]
for i in range(1,N):
    P[i] += P[i-1]
P.insert(0,0)
for _ in range(Q):
    L, R = map(int, I().split())
    print(P[R]-P[L-1])