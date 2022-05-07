import sys
from collections import defaultdict
N, S = sys.stdin.read().split()
N = int(N)
s, e = 0, 0
ans, L = 1, len(S)
kind = defaultdict(int)
while s<L and e<L:
    kind[S[e]] += 1
    if N >= len(kind):
        ans = max(ans, e-s+1)
    else:
        while s<=e and len(kind)>N:
            if kind[S[s]]:
                kind[S[s]] -= 1
            if not kind[S[s]]:
                kind.pop(S[s])
            s += 1
    e += 1
print(ans)