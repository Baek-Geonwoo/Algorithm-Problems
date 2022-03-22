import sys
from collections import Counter
N, *A = map(int, sys.stdin.read().split())
A.sort()
print(round(sum(A)/N))
print(A[N//2])
C = Counter(A).most_common()
if N > 1:
    if C[0][1] == C[1][1]:
        print(C[1][0])
    else:
        print(C[0][0])
    print(A[-1]-A[0])
else:
    print(A[0])
    print(0)