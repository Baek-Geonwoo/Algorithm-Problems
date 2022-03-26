import sys
def check(K):
    cnt = 0
    for t in T:
        cnt += K // t
    if cnt >= M: return True
    return False
N, M, *T = map(int, sys.stdin.read().split())
lo, hi = 0, int(1e18)
while lo+1<hi:
    mid = (lo + hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)