import sys
def check(m):
    if m < mx: return False
    cnt = 1
    curr = 0
    for b in B:
        if curr+b > m:
            cnt += 1
            curr = 0
        curr += b
    if cnt <= M: return True
    return False
N, M, *B = map(int, sys.stdin.read().split())
lo, hi = 0, sum(B)
mx = max(B)
while lo+1<hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)