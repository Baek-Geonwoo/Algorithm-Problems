import sys
I = sys.stdin.readline
N, M = map(int, I().split())
A = [int(e) for e in I().split()]
B = [int(e) for e in I().split()]
a, b = 0, 0
while a < N and b < M:
    if A[a] < B[b]:
        print(A[a], end=" ")
        a += 1
    else:
        print(B[b], end=" ")
        b += 1
for i in range(a,N):
    print(A[i], end=" ")
for i in range(b,M):
    print(B[i], end=" ")