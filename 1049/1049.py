import sys
I = sys.stdin.readline
N, M = map(int, I().split())
S = [list(map(int, I().split())) for _ in range(M)]
Set, EA = 100*6, 100
m = 1000*N
for s, i in S:
    Set = min(Set, s)
    EA = min(EA, i)
print(min(Set*(N//6+1), Set*(N//6) + EA*(N%6), EA*N))