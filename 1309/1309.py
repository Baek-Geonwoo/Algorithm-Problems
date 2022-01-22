import sys
n = int(sys.stdin.readline())
P = [0]*(n+1)
P[1] = 3
if n >= 2:
    P[2] = 7
for i in range(3,n+1):
    P[i] = (P[i-1]*2 + P[i-2])%9901
print(P[n])