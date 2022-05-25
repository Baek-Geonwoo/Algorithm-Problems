import sys
from collections import deque
S = sys.stdin.readline().rstrip()
stack = deque()
ans = 0
tmp = 1
dct = {'(':2, '[':3}
for i in range(len(S)):
    if S[i] in '[(':
        stack.append(S[i])
        tmp *= dct[S[i]]
    else:
        if not stack:
            ans = 0
            break
        if S[i] == ')' and stack[-1] == '(':
            if S[i-1] == '(':
                ans += tmp
            stack.pop()
            tmp //= 2
        elif S[i] == ']' and stack[-1] == '[':
            if S[i-1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
        else:
            ans = 0
            break
if stack:
    print(0)
else:
    print(ans)