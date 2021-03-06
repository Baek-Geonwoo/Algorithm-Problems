import sys
def check(m):
    n = 0
    d = 5
    while d<=m:
        n += m//d
        d *= 5
    return n
M = int(sys.stdin.readline())
lo, hi = 1, 500000000
ans = -1
flag = False
while lo<=hi:
    mid = (lo+hi)//2
    n = check(mid)
    if n >= M:
        if M == n:
            ans = mid
            flag = True
        hi = mid-1
    else:
        lo = mid+1
if flag:
    print(ans)
else:
    print(-1)