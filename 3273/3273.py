import sys
N, *A, x = map(int, sys.stdin.read().split())
A.sort()
L, R = 0, N-1
ans = 0
while L < R:
    S = A[L] + A[R]
    if S == x: ans += 1
    if S < x: L += 1
    else: R -= 1
print(ans)