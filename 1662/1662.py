import sys
from collections import deque
S = sys.stdin.readline().rstrip()
stack = deque()
ans = 0
for s in S:
    if s == '(':
        stack.append((K,ans-1))
        ans = 0
    elif s == ')':
        K, prev = stack.pop()
        ans = K*ans+prev
    else:
        K = int(s)
        ans += 1
print(ans)