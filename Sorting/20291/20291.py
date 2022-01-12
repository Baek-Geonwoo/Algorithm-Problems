import sys
I = sys.stdin.readline
n = int(I())
E = {}
for i in range(n):
    e = I().strip('\n').split(".")[1]
    try:
        E[e] += 1
    except:
        E[e] = 1
for e in sorted(E.keys()):
    print(e,E[e])