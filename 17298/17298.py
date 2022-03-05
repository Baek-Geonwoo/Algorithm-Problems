import sys
from collections import deque
N, *A = map(int,sys.stdin.read().split())
O = ['-1']*N
stack = deque((A[-1],))
for i in range(N-2,-1,-1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack:
        O[i] = str(stack[-1])
    stack.append(A[i])
print(" ".join(O))