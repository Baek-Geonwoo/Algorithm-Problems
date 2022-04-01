import sys
def pieces(mid):
    return (mid+1)*(n-mid+1)
n, k = map(int, sys.stdin.readline().split())
lo, hi = 0, n+1
while lo+1<hi:
    mid = (lo+hi)//2
    if pieces(mid) == k:
        print('YES'); sys.exit()
    elif pieces(mid) > k: hi = mid
    else: lo = mid
print('NO')