import sys
from collections import deque
N, *A = map(int, sys.stdin.read().split())
A = deque(sorted(A))
ans = 0
if N%2:
    ans += A[N//2]
    A.remove(A[N//2])
while A:
    A.popleft()
    ans += A.pop()*2
print(ans)