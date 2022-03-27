import sys
def check(x):
    S = x*(x+1)//2
    for i in range(N-1):
        d = min(x, A[i+1]-A[i])
        S += d*(x+x-d+1)//2
        if S >= K:
            return True
    if S >= K:
        return True
    return False
N, K, *A = map(int, sys.stdin.read().split())
lo, hi = 0, int(1e18)
while lo+1<hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)