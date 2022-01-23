import sys
I = sys.stdin.readline
N, L = map(int, I().split())
H = [int(e) for e in I().split()]
H.sort()
for h in H:
    if h <= L:
        L += 1
    else:
        break
print(L)