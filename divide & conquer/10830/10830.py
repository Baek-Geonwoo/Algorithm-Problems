import sys
input = sys.stdin.readline
def mul(A,B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    for i in range(n):
        for j in range(n):
            C[i][j] %= 1000
    return C
def matrix_pow(M,b):
    n = len(M)
    if b == 1:
        return M
    elif b == 2:
        return mul(M,M)
    else:
        N = matrix_pow(M,b//2)
        if b%2:
            return mul(mul(N,N),M)
        return mul(N,N)

n, b = map(int,input().split())
A = []
for i in range(n):
    A.append([int(e) for e in input().split()])
M = matrix_pow(A,b)
for i in range(n):
    for j in range(n):
        print(M[i][j]%1000,end=" ")
    print()