import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    n, m = map(int, I().split())
    A = [int(e) for e in I().split()]
    B = [int(e) for e in I().split()]
    A.sort()
    B.sort()
    cnt = 0
    a, b = n-1, m-1
    while a>=0 and b>=0:
        if A[a] > B[b]:
            cnt += b+1
            a -= 1
        else:
            b -= 1
    print(cnt)