import sys
N = int(sys.stdin.readline())
S = set()
for i in range(N+1):
    for v in range(N-i+1):
        for x in range(N-i-v+1):
            l = N - i - v - x
            ans = 1*i + 5*v + 10*x + 50*l
            S.add(ans)
print(len(S))