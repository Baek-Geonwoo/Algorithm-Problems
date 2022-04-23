import sys
N = int(sys.stdin.readline())
lo, hi = 1, N
while lo<=hi:
    mid = (lo+hi)//2
    if N <= mid**2:
        hi = mid-1
    else:
        lo = mid+1
print(lo)