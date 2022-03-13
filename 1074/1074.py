import sys
def Z(n, r, c):
    if n == 0:
        return 0
    for i in range(2):
        for j in range(2):
            if r < (i+1)*n and c < (j+1)*n:
                return (i*2+j)*n**2 + Z(n//2, r-i*n, c-j*n)
N, r, c = map(int, sys.stdin.readline().split())
print(Z(2**(N-1),r,c))