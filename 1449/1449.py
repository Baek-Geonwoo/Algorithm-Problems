import sys
I = sys.stdin.readline
N, L = map(int, I().split())
A = [int(e) for e in I().split()]
A.sort()
pos = 0
ans = 0
for a in A:
    if pos < a:
        ans += 1
        pos = a+L-1
print(ans)