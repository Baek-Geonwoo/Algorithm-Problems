import sys
I = sys.stdin.readline
T = int(I())
for t in range(1,T+1):
    N = int(I())
    A = [int(e) for e in I().split()]
    D = []
    for _ in range(N):
        d = A[0]
        D.append(A[0])
        A.pop(0)
        for i in range(len(A)):
            if A[i] == d*4//3:
                A.pop(i)
                break
    print("Case #{}:".format(t)+" ".join(map(str,D)))