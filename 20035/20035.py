import sys
def I():
    return map(int, sys.stdin.readline().split())
N, M = I()
A = list(I())
B = list(I())
m = max(A)
lo = A.index(m)
hi = N-1-list(reversed(A)).index(m)
print((sum(A)+m*(M-1))*10**9+sum(B)+B[0]*lo+max(B)*(hi-lo)+B[-1]*(N-1-hi))