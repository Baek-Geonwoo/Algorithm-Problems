import sys
def check(m):
    cut = 0
    left = 0
    for right in S:
        if right-left>=m:
            left = right
            cut += 1
    if cut > Q: return True
    return False
I = sys.stdin.readline
N, M, L = map(int, I().split())
S = [int(I()) for _ in range(M)]+[L]
for _ in range(N):
    Q = int(I())
    lo, hi = 0, L
    while lo+1<hi:
        mid = (lo+hi)//2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)