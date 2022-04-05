import sys
def check(s):
    L, R = 0, 0
    for l,r in A:
        if l <= s:
            L += l; R += min(r,s)
        else: return False
    if L <= T <= R:
        return True
    else:
        return False
I = sys.stdin.readline
N, T = map(int, I().split())
A = [tuple(map(int, I().split())) for _ in range(N)]
lo, hi = 1, 1000000
while lo<=hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid-1
    else:
        lo = mid+1
print(-1 if lo == 1000001 else lo)