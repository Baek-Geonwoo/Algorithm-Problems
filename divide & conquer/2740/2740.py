import sys
input = sys.stdin.readline
n, m = map(int,input().split())
A = []
for i in range(n):
    A.append([int(e) for e in input().split()])
m, k = map(int,input().split())
B = []
for i in range(m):
    B.append([int(e) for e in input().split()])
C = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for h in range(m):
            C[i][j] += A[i][h]*B[h][j]
        print(C[i][j], end=" ")
    print()