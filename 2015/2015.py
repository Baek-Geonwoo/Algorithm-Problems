import sys
from collections import defaultdict
N, K, *A = map(int, sys.stdin.read().split())
dct = defaultdict(int)
dct[0] = 1
pSum = 0
ans = 0
for a in A:
    pSum += a
    if pSum-K in dct: ans += dct[pSum-K]
    dct[pSum] += 1
print(ans)