import sys
I = sys.stdin.readline
N, M = map(int, I().split())
B = [int(e) for e in I().split()]
B.sort()
ans = -max(abs(B[0]),B[-1])
p = -1
for i in range(N):
    if B[i]>0:
        p = i
        break
if p == -1:
    p = N
for i in range(0,p,M):
    ans += -B[i]*2
for i in range(N-1,p-1,-M):
    ans += B[i]*2
print(ans)