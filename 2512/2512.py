import sys
I = sys.stdin.readline
N = int(I())
A = [int(e) for e in I().split()]
M = int(I())
if sum(A) <= M:
    print(max(A))
else:
    low, high = 1, max(A)
    while low <= high:
        m = (low + high)//2
        Sum = sum([min(m,a) for a in A])
        if Sum <= M:
            low = m+1
        else:
            high = m-1
    print(high)