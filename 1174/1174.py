import sys
from itertools import combinations
N = int(sys.stdin.readline())
C = []
for i in range(1,11):
    for c in combinations(range(10), i):
        temp = sorted(c)
        I, d = 0, 1
        for t in temp:
            I += t*d
            d *= 10
        C.append(I)
C.sort()
try:
    print(C[N-1])
except:
    print(-1)