import sys
I = sys.stdin.readline
n = int(I())
m = int(I())
A = [int(e) for e in I().split()]
A.sort()
s,e = 0, n-1
cnt = 0
while s <= e:
    if A[s]+A[e] == m:
        cnt += 1
        s += 1
        e -= 1
    elif A[s]+A[e] < m:
        s += 1
    else:
        e -= 1
print(cnt)