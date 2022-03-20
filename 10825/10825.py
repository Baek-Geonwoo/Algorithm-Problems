import sys
I = sys.stdin.readline
N = int(I())
A = []
for _ in range(N):
    name, *score = I().split()
    A.append([name] + list(map(int,score)))
A.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for a in A:
    print(a[0])