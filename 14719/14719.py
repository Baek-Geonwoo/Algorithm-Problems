import sys
H, W, *B = map(int, sys.stdin.read().split())
A = [0]*W
high = B[0]
for i in range(1,W-1):
    A[i] = max(0,high-B[i])
    high = max(high,B[i])
high = B[-1]
for i in range(W-2,0,-1):
    A[i] = min(A[i],max(0,high-B[i]))
    high = max(high,B[i])
print(sum(A))