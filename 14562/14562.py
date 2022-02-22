import sys
from collections import deque
I = sys.stdin.readline
C = int(I())
for _ in range(C):
    S, T = map(int, I().split())
    Q = deque(((S,T,0),))
    ans = 10000
    while Q:
        S, T, k = Q.pop()
        if S == T:
            ans = min(ans,k)
            continue
        if S < T:
            Q.appendleft((S+1, T, k+1))
        if S*2 <= T+3:
            Q.appendleft((S*2, T+3, k+1))
    print(ans)