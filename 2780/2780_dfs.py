import sys
T, *L = map(int, sys.stdin.read().split())
K = {
    1:(2,4),2:(1,3,5),3:(2,6),
    4:(1,5,7),5:(2,4,6,8),6:(3,5,9),
    7:(0,4,8),8:(5,7,9),9:(6,8),
    0:(7,)
}
mod = 1234567
for t in range(T):
    N = L[t]
    P = [1]*10
    C = [0]*10
    for _ in range(1,N):
        for i in range(10):
            for k in K[i]:
                C[i] += P[k]
        P = [c%mod for c in C]
        C = [0]*10
    print(sum(P)%mod)