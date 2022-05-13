import sys
from itertools import combinations
input = sys.stdin.readline
N, L, R, X = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(2,N+1):
    for c in combinations(A,i):
        if L <= sum(c) <= R and c[-1]-c[0] >= X:
            ans += 1
print(ans)