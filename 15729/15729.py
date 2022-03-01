import sys
I = sys.stdin.readline
N = int(I())
R = [int(e) for e in I().split()]
cnt = 0
for i in range(N):
    if R[i]:
        R[i] = 0
        if i+1<N:
            R[i+1] = (R[i+1]+1)%2
        if i+2<N:
            R[i+2] = (R[i+2]+1)%2
        cnt += 1
print(cnt)