import sys
I = sys.stdin.readline
n = int(I())
A = [int(e) for e in I().split()]
B = [int(e) for e in I().split()]
A.sort()
B.sort(reverse=True)
S = 0
for i in range(n):
    S += A[i]*B[i]
print(S)