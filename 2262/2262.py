import sys
n, *A = map(int, sys.stdin.read().split())
ans = 0
for i in range(n,1,-1):
    idx = A.index(i)
    if idx == len(A)-1:
        ans += A[idx] - A[idx-1]
    elif idx == 0:
        ans += A[idx] - A[idx+1]
    else:
        ans += A[idx] - max(A[idx-1], A[idx+1])
    A.pop(idx)
print(ans)