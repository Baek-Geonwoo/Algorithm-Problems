import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    n = int(I())
    A = [[int(e) for e in I().split()] for _ in range(n)]
    A.sort()
    print(A)
    admit = 1
    max_score = A[0][1]
    for i in range(1,n):
        if A[i][1]>max_score:
            admit += 1
            max_score = A[i][1]
    print(admit)