import sys
N, K, T, *A = map(int, sys.stdin.read().split())
A.sort()
s, e = 0, N-1; cnt = 0
while s < e and cnt < T:
    if A[s] < K-A[e]:
        A[e] += A[s]
        cnt += A[s]
        A[s] = 0
        s += 1
    elif A[s] == K-A[e]:
        A[e] += A[s]
        cnt += A[s]
        A[s] = 0
        s += 1
        A[e] = 0
        e -= 1
    else:
        A[s] -= K-A[e]
        cnt += K-A[e]
        A[e] = 0
        e -= 1
print("YES") if cnt <= T and sum(A)==0 else print("NO")