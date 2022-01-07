import sys
input = sys.stdin.readline
def mul(A,B):
    C = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
    for i in range(2):
        for j in range(2):
            C[i][j] %= 1000000007
    return C
def matrix_pow(M,b):
    if b == 1:
        return M
    elif b == 2:
        return mul(M,M)
    else:
        N = matrix_pow(M,b//2)
        if b%2:
            return mul(mul(N,N),M)
        return mul(N,N)
n = int(input())
F = [[1],[0]] #F1과 F0
A = [[1,1],[1,0]] #Fn을 구할 때 필요한 2x2행렬
if n > 1:
    M = matrix_pow(A,n-1)
    B = [[0],[0]]
    for i in range(2):
        for j in range(2):
            B[i][0] += M[i][j]*F[j][0]
        B[i][0] %= 1000000007
    print(B[0][0])
else:
    print(F[-n-1])