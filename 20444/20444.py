import sys
def pieces(mid):
    return (mid+1)*(n-mid+1)
n, k = map(int, sys.stdin.readline().split())
lo, hi = 0, n//2
while lo<=hi:
    mid = (lo+hi)//2
    if pieces(mid) == k:
        print('YES'); sys.exit()
    elif pieces(mid) > k: hi = mid-1
    else: lo = mid+1
print('NO')