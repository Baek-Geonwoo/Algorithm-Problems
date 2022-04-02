import sys
n, *A = map(int, sys.stdin.read().split())
A.sort()
ans = 0
curr = sum(A)
for i in range(n-1):
    curr -= A[i]
    ans += A[i]*curr
print(ans)