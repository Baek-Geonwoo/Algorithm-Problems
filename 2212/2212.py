import sys
from heapq import heappush, heappop
N, K, *A = map(int, sys.stdin.read().split())
H = []
A.sort()
for i in range(N-1):
    if len(H) < K-1:
        heappush(H, A[i+1]-A[i])
    else:
        heappush(H, A[i+1]-A[i])
        heappop(H)
print(A[-1] - A[0] - sum(H))