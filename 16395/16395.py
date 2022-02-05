import sys
n, k = map(int, sys.stdin.readline().split())
C = [[1]*(i+1) for i in range(n)]
for i in range(2,n):
    for j in range(1,i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]
print(C[n-1][k-1])